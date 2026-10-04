import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "seal_report.py"


class SealTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.report = self.root / "报告.md"
        self.data = "Evidence: alpha.\n".encode()
        self.report.write_bytes(self.data)
        self.seal = self.root / "report.seal.json"

    def cli(self, *args):
        return subprocess.run([sys.executable, "-B", "-X", "utf8", str(SCRIPT),
                               str(self.report), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8")

    def create(self):
        result = self.cli("--write-sidecar", self.seal)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_round_trip_preserves_report(self):
        self.create()
        self.assertEqual(self.cli("--verify-sidecar", self.seal).returncode, 0)
        self.assertEqual(self.report.read_bytes(), self.data)

    def test_same_size_content_change_fails(self):
        self.create()
        self.report.write_bytes(self.data.replace(b"alpha", b"bravo"))
        self.assertEqual(self.cli("--verify-sidecar", self.seal).returncode, 2)

    def test_changed_length_fails(self):
        self.create()
        self.report.write_bytes(self.data + b"more")
        self.assertEqual(self.cli("--verify-sidecar", self.seal).returncode, 2)

    def test_identical_bytes_at_different_path_fail(self):
        self.create()
        other = self.root / "copy.md"
        other.write_bytes(self.data)
        self.report = other
        self.assertEqual(self.cli("--verify-sidecar", self.seal).returncode, 2)

    def test_input_cannot_be_sidecar(self):
        self.assertEqual(self.cli("--write-sidecar", self.report).returncode, 2)
        self.assertEqual(self.report.read_bytes(), self.data)

    def test_existing_sidecar_is_preserved(self):
        self.create()
        before = self.seal.read_bytes()
        self.report.write_bytes(b"new report")
        self.assertEqual(self.cli("--write-sidecar", self.seal).returncode, 2)
        self.assertEqual(self.seal.read_bytes(), before)

    def test_wrong_expected_digest_creates_nothing(self):
        result = self.cli("--expect", "0" * 64, "--write-sidecar", self.seal)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(self.seal.exists())

    def test_expected_digest_accepts_lowercase(self):
        self.assertEqual(self.cli("--expect", hashlib.sha256(self.data).hexdigest()).returncode, 0)

    def test_malformed_sidecars_fail_cleanly(self):
        for value in ("{", "[]", "null", '{"schema_version": 2}',
                      '{"schema_version": 1, "bytes": true}'):
            with self.subTest(value=value):
                self.seal.write_text(value, encoding="utf-8")
                result = self.cli("--verify-sidecar", self.seal)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)

    def test_verify_and_write_cannot_be_combined(self):
        self.create()
        before = self.seal.read_bytes()
        self.assertEqual(self.cli("--verify-sidecar", self.seal,
                                  "--write-sidecar", self.seal).returncode, 2)
        self.assertEqual(self.seal.read_bytes(), before)

    def test_missing_input_does_not_create_seal(self):
        self.report.unlink()
        self.assertEqual(self.cli("--write-sidecar", self.seal).returncode, 2)
        self.assertFalse(self.seal.exists())

    def test_unknown_schema_is_rejected_even_with_matching_content(self):
        self.create()
        value = json.loads(self.seal.read_text(encoding="utf-8"))
        value["schema_version"] = 99
        self.seal.write_text(json.dumps(value), encoding="utf-8")
        self.assertEqual(self.cli("--verify-sidecar", self.seal).returncode, 2)


if __name__ == "__main__":
    unittest.main()

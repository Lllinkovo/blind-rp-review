#!/usr/bin/env python3
"""Seal or verify local review bytes; seals do not attest review quality."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re


def sha256_file(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(chunk)
            digest.update(chunk)
    return size, digest.hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Report or proposal to check")
    parser.add_argument("--expect", help="Expected SHA-256; mismatch exits 2")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write-sidecar", type=Path, help="Create a new seal; never overwrite")
    mode.add_argument("--verify-sidecar", type=Path, help="Verify an existing seal")
    args = parser.parse_args()
    if args.expect is not None and not re.fullmatch(r"[0-9a-fA-F]{64}", args.expect):
        parser.error("--expect must contain exactly 64 hexadecimal characters")
    try:
        path = args.path.resolve(strict=True)
        if not path.is_file():
            raise ValueError("input must be a regular file")
        size, digest = sha256_file(path)
        record = {"schema_version": 1, "path": str(path), "bytes": size, "sha256": digest}
        matches = args.expect is None or digest == args.expect.upper()
        if args.verify_sidecar is not None:
            expected = json.loads(args.verify_sidecar.read_text(encoding="utf-8"))
            if not isinstance(expected, dict):
                raise ValueError("seal must be a JSON object")
            if type(expected.get("schema_version")) is not int or expected["schema_version"] != 1:
                raise ValueError("unsupported seal schema")
            if type(expected.get("bytes")) is not int or expected["bytes"] < 0:
                raise ValueError("invalid seal byte count")
            if not isinstance(expected.get("path"), str):
                raise ValueError("invalid seal path")
            if not isinstance(expected.get("sha256"), str) or not re.fullmatch(r"[0-9A-F]{64}", expected["sha256"]):
                raise ValueError("invalid seal digest")
            matches = matches and all(expected[key] == record[key] for key in record)
        if args.write_sidecar is not None:
            target = args.write_sidecar.resolve()
            if target == path or (target.exists() and target.samefile(path)):
                raise ValueError("sidecar cannot replace the input")
            if not matches:
                raise ValueError("expected digest does not match; no sidecar written")
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({**record, "expected_match": matches}, ensure_ascii=False, indent=2))
        return 0 if matches else 2
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

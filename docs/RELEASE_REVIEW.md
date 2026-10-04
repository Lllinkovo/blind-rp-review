# Release review

Prepared: 2026-10-03. Updated: 2026-10-04. Scope: first experimental public preview.

Repository: [Lllinkovo/blind-rp-review](https://github.com/Lllinkovo/blind-rp-review).

## Ready for inspection

- A standalone entrypoint with four audit modules and an adjudicator.
- Explicit meanings for independent and reduced-isolation modes.
- Standard-library seal CLI with input preservation and exclusive sidecar creation.
- Synthetic cases, held-separate expected findings, and mechanical tests.
- Chinese and English overview documentation.

## Publication scope

The public maintainer is Lllinkovo. Upstream ARS review concepts are credited in PROVENANCE.md; the upstream copyright, license, and warranty disclaimer are preserved. The adaptation is distributed under CC BY-NC 4.0.

The preview includes the skill, supporting protocol, CLI and tests, synthetic fixtures, and documentation. It excludes private preparation logs, actual applicant proposals, correspondence, and runtime seal files.

## Next validation work

1. Run a fresh-context behavioral pilot on the three synthetic cases.
2. Compare the standalone skill with the earlier ARS-backed workflow on matched inputs.
3. Publish observed detection, severity disagreements, host limitations, and failure cases.

These items are planned work. The public preview carries no claims of completed behavioral validation.

## What has changed from the installed prototype

- ARS is no longer a required runtime dependency in the standalone candidate. This changes its review context and needs behavioral comparison.
- Hash checks now cover the proposal and neutral manifest before adjudication.
- Context independence and instruction-based file restrictions are described separately.
- Reduced-isolation assessments are allowed only with their declared status; an independent run with a breach is invalid.
- The seal tool rejects source-file overwrite, existing-sidecar overwrite, malformed seals, and a mismatched expected hash before creating a sidecar.

The installed skill has not been changed. Passing mechanical checks does not establish scholarly validity, predictive accuracy, or equivalence to the earlier ARS-backed workflow.

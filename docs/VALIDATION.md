# Validation record

Updated: 2026-10-04. Scope: experimental preview.

| Check | Observed result |
|---|---|
| Seal CLI tests | 12 passed during publication preparation; executable code unchanged in this documentation update |
| Python and JSON parsing | Passed |
| Internal Markdown links | Checked after adding the demonstration |
| Basic frontmatter inspection | Name and quoted description checked |
| Official skill validator | Not completed: required PyYAML unavailable in the validation environment |
| Known private identifiers and absolute-path scan | Checked on the publication text, including the demonstration |
| Installed source preservation | Original installed skill untouched |
| Fresh-context demonstration | C1 completed through S1–S4 and S5; exact record in [DEMO.md](DEMO.md) |
| Skill installation / automatic discovery | Not tested by this run; the coordinating Agent explicitly followed the package protocol |
| C2 and C3 behavioral runs | Not run |
| Repeatability across models or runs | Not measured |
| Matched baseline or scholarly accuracy comparison | Not run |
| Expert scoring / expected-label comparison | Not performed for this demonstration |
| License | CC BY-NC 4.0 with upstream attribution and modification notes |

## Mechanical test coverage

The 12 CLI tests cover unchanged files, same-length edits, length changes,
path changes, accidental input overwrite, existing-sidecar overwrite,
expected-hash mismatch, lowercase expected hashes, malformed records,
conflicting command modes, missing input, and an unsupported schema.

Run from the repository root:

```bash
python -B -m unittest discover -s tests -v
```

## Demonstration scope

C1 is a short fictional diagnostic excerpt, not a complete PhD application. Reviewers received their declared inputs in fresh contexts without parent-history inheritance. Their file access limits were instruction-based, not separate filesystem sandboxes. S5 started after the coordinator verified the proposal, S0 and all four specialist reports; S5 was then sealed and verified too.

The demonstration contains actual model-generated reports. Its result is evidence about this run, not an accuracy estimate or an expert endorsement. The expected labels remain separate, and they were not used to write or revise the frozen reports.

Private-path scanning is a targeted check, not a universal guarantee. Raw local seal sidecars are kept out of the public package.

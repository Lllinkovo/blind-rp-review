# Release scope and next steps

Updated: 2026-10-04. Status: experimental public preview.

Repository: [Lllinkovo/blind-rp-review](https://github.com/Lllinkovo/blind-rp-review).

## Included

- A standalone skill entrypoint, four specialist modules, an adjudicator, and an output schema.
- Explicit fresh-context and reduced-isolation modes.
- A standard-library sealing CLI with input-preservation and overwrite checks.
- Three synthetic input fixtures and evaluator-only expected findings.
- Bilingual setup and project documentation.
- An actual C1 demonstration with recorded inputs, specialist reports, adjudication, and seal checks; see [DEMO.md](DEMO.md).

The public maintainer is Lllinkovo. Upstream ARS review concepts are credited in [PROVENANCE.md](../PROVENANCE.md). Copyright, license, and warranty attribution are retained. Distribution uses CC BY-NC 4.0.

## What the demonstration establishes

The recorded host can run this bounded example through separate specialist contexts and a subsequent adjudication step. The public demonstration preserves observed outputs. It is one short fictional case, with no repeated trials, expert scoring, or matched baseline.

See [VALIDATION.md](VALIDATION.md) for the exact state of mechanical and behavioral checks.

## Next maintenance priorities

1. Run the other two fixtures, recording misses, unsupported findings, and severity disputes.
2. Compare matched runs with and without the skill, and with the earlier ARS-backed workflow. Keep input, model and tools fixed and report differences in computational budget.
3. Convert observed failures into regression cases; reserve new unseen cases for later evaluation.

These are planned tasks. No recurring automation is enabled by this roadmap.

## Changes from the installed prototype

- Selected ARS review concepts are adapted into included modules; ARS is no longer a runtime dependency.
- Seals cover the proposal, S0 and reports before adjudication.
- Context independence and instruction-based file restrictions are documented separately.
- A declared reduced-isolation mode is available when fresh contexts are unavailable.
- The CLI rejects accidental input overwrite, existing-sidecar overwrite, malformed seals and an expected-hash mismatch.
- Documentation now includes concrete setup commands, an actual run, and a source-based account of the project's contribution.

The original installed skill is unchanged. Private proposals, correspondence, preparation logs and absolute-path seal sidecars are excluded from the public package.

---
name: stress-test-phd-rp
description: "Review a PhD research proposal through separate audits of its question, contribution, sources, and methods, then adjudicate frozen findings. Use for RP blind review, 高压审核 RP, 最强拒稿理由, or 高压复审. Keep prior reviews and human feedback hidden until the verdict is frozen."
---

# Blind RP Review

Find the strongest defensible objection to a PhD research proposal and test whether it survives the proposal's best supported defence. Return located findings and an actionable decision.

## Define the run

Read [review-protocol.md](references/review-protocol.md) and [output-schema.md](references/output-schema.md). The included modules supply the review criteria; no other academic skill is required for the standalone workflow.

Use the exact user-selected proposal. Review a concept note in proportion to its genre and length. Write reports in the requested language, or the language of the user's request. Keep the proposal unchanged. Editing, submission, or sending requires the user's corresponding request.

Here, **blind** means specialists cannot see prior reviews, human feedback, expected answers, the author's preferred verdict, or the parent conversation. It does not automatically anonymize the author. Separate contexts can still share model biases.

Check the host's capabilities before claiming isolation:

- Fresh child contexts with no inherited conversation are needed for `INDEPENDENT_MODULES`.
- Use an exact input allowlist and prohibit discovery, memory, and other reviewers' files. Record whether the boundary is technically enforced or instruction-based. An instruction-only allowlist is not a filesystem sandbox.
- If fresh contexts cannot be created, use `REDUCED_ISOLATION_SINGLE_CONTEXT` from the start. Follow the same criteria and disclose the reduced isolation.
- If a run claims independent isolation and that boundary is breached, use `RUN_INVALID_ISOLATION_FAILURE`. Preserve completed reports and rerun affected work under valid boundaries before issuing a canonical verdict.

For PDF or DOCX, use available local document tools. Record page or paragraph locators and unreadable content. Do not send proposal text to additional services or external models without authorization. The host's normal model processing still applies; this skill does not make a cloud model local.

## 1. Lock the proposal and frame

Create a separate run folder. In `S0_MANIFEST.md`, record:

- proposal path, byte count, SHA-256, genre, and word or page extent;
- extraction method and unavailable material;
- programme constraints supplied by the user;
- neutral section map and load-bearing claim inventory, with no verdict;
- allowed public-source verification and exact input paths for each role;
- isolation mode and enforcement method.

Seal and verify S0 using the commands below. Seal the proposal too, storing its sidecar in the run folder. Sidecars are local records and may contain private absolute paths.

## 2. Run four specialist audits

Use fresh contexts with no inherited conversation when supported. A role receives only the proposal and seal, S0 and seal, common protocol, output schema, and its own module:

| Role | Read |
|---|---|
| S1: object, question, field | [S1](references/modules/s1-object-problem-field.md) |
| S2: literature, gap, contribution | [S2](references/modules/s2-literature-gap-contribution.md) |
| S3: claims and cited sources | [S3](references/modules/s3-claim-source.md) |
| S4: methods, inference, access | [S4](references/modules/s4-method-inference-access.md) |

Do not give specialists another role's specification or report. Public-source browsing is permitted only for S3 when authorized. Use bibliographic queries rather than private proposal passages. Verified source passages and locators belong in S3's report so the adjudicator can assess evidence without new browsing.

Keep at most two specialist audits running at once and at most four agents including the coordinator; tighter host limits apply. Otherwise work sequentially in fresh contexts.

Each specialist writes `Sx_REPORT.md`, verifies proposal and S0 seals, and records any input-boundary breach. The coordinator seals and verifies each completed report before adjudication. Record dispatch, role IDs, declared inputs, and completion in a separate run log, leaving sealed S0 unchanged.

```text
python scripts/seal_report.py run/S1_REPORT.md --write-sidecar run/S1_REPORT.seal.json
python scripts/seal_report.py run/S1_REPORT.md --verify-sidecar run/S1_REPORT.seal.json
```

Repeat for S0, S2-S4, and the proposal with exact paths. Run commands from the skill root or use an absolute script path. A sidecar is created once; deliberate revision needs a new version and sidecar.

## 3. Adjudicate frozen findings

Reverify the proposal, S0, and S1-S4 before starting S5. Record successful checks and actual context-boundary evidence in the run log.

Give S5 a fresh context with only the proposal and seal, S0 and seal, protocol, schema, [S5](references/modules/s5-adjudicator.md), S1-S4 and their seals, and a bounded dispatch/completion record establishing the declared mode and order. Exclude human feedback, expected answers, parent history, and other workspace files.

S5 must:

- trace decisive findings to the proposal and a frozen report;
- merge duplicates and resolve disagreements;
- run two concrete counter-tests for each proposed PASS;
- retain BLOCK only with an exact locator, failed condition, central consequence, strongest defence, reason that defence fails, and separate detection/severity confidence;
- downgrade when a credible fallback preserves the central question, contribution, and valid inference;
- freeze the verdict before strengths and repair advice.

Do not average scores or let majority voting erase unresolved critical defects. Hash verification checks bytes against a stored record; it does not prove isolation, authorship, or scholarly correctness.

Seal and verify `S5_REPORT.md` before presenting it as frozen. A planned reduced-isolation run may produce a clearly labelled assessment. A breached independent run cannot be silently presented as valid.

## 4. Return the decision

Use the output schema. Deliver the review, exact reviewed version, isolation mode, important unknowns, and up to three prioritized repairs.

- `BLOCK`: a demonstrated central failure survives its strongest credible defence.
- `MAJOR REVISION`: material weaknesses remain, with a plausible repair preserving the project.
- `PASS FOR HUMAN REVIEW`: no unresolved critical or major defect survived this bounded review.

Missing full text stays `UNKNOWN` unless a material contradiction or unmet proof burden is established. Field-norm findings need a checkable boundary and an explanation of how the proposal crosses it. A review pass does not predict admission or publication.

## Revision and calibration

For re-review, test old findings against the new version and scan for new defects. Label it a re-review because old findings are visible.

For human-feedback calibration, freeze the blind report first. Only a separate post-freeze evaluator may read human comments or expected answers. Compare concerns as `FULL`, `PARTIAL`, `MISS`, or `CONTRADICTED`, including severity errors and false reassurance. Preserve the original verdict.

The repository's `evals/expected.json` is evaluator-only material. Never pass it to a blind reviewer. See [the evaluation guide](docs/EVALUATION.md) when explicitly testing this skill.

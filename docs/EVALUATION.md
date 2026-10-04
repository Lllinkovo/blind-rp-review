# Evaluation

## Two separate checks

1. **Mechanical checks:** command-line seals detect changed bytes, reject invalid records, preserve the input, and refuse to overwrite existing seals.
2. **Review behavior:** fresh reviewers identify material problems without seeing expected findings or previous feedback.

Passing (1) does not establish (2). A single fresh-context demonstration of C1 is recorded in [DEMO.md](DEMO.md), including the actual specialist and adjudicator outputs. C2 and C3 have not been run. The C1 demonstration was not scored against the expectation file and is not an accuracy benchmark.

## Synthetic fixtures

Give a reviewer only the selected proposal, the skill's runtime instructions, and that run's allowed files.

| Case | Reviewer input |
|---|---|
| C1 | [proposal](../examples/case-01/proposal.md) |
| C2 | [proposal](../examples/case-02/proposal.md) |
| C3 | [proposal](../examples/case-03/proposal.md) |

Keep `evals/expected.json` hidden. Do not put case descriptions, expected severity, or evaluator prompts into S0. If the reviewer has already read expectations in the current conversation, use a fresh context.

These are diagnostic excerpts, not complete applications. Review the declared claim and design; do not infer a missing full proposal or demand sections outside the stated scope.

## Run protocol

1. Record skill revision/hash, host, model identifier if available, date, isolation mode, allowed inputs, and browsing permission.
2. Run each fixture in a fresh context. Keep prior outputs and human labels hidden.
3. Preserve and seal S0-S5 and the exact input.
4. After S5 is frozen, give the evaluator the report and expected findings.
5. Report each expected concern as FULL, PARTIAL, MISS, or CONTRADICTED. Record extra unsupported findings, severity disagreement, and quotations supporting the evaluation.
6. Record elapsed time and tool/model cost only if observed. Do not invent estimates.

For a skill/no-skill comparison, keep proposal, model, tool access, and requested task fixed. Use separate fresh contexts and report differences in agent count and token allowance; otherwise any change may reflect extra computation rather than the instructions. Preserve both reports and publish the small sample size.

Once a case has informed revisions, treat it as a regression case. Evaluate later changes on new held-out cases as well.

## Useful outcomes

- Detection: the material issue is identified at the correct location.
- Severity calibration: a repairable limitation is not automatically fatal.
- Evidence discipline: unavailable source text stays unknown.
- Isolation: dispatch records support the declared context boundaries.
- Stability: sealed inputs and reports still match at adjudication.

Expected labels are provisional author-written fixtures, not an expert gold standard. A reviewer may disagree with a label if its evidence supports the disagreement; record that instead of forcing a pass.

## Public demonstration and future evaluations

The published C1 reports make the case visible as a worked example. Keep those reports out of reviewer inputs when reproducing the mechanics. Use new, unrevealed cases for claims about generalization. Do not retroactively rewrite a frozen report to match its expected label.

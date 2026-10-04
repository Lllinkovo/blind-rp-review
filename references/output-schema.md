# Output Schema

Use this order. Do not put strengths or remedies before the frozen verdict.

## 1. 审核结论

- **Verdict:** `BLOCK` / `MAJOR REVISION` / `PASS FOR HUMAN REVIEW`
- **一句话理由:** the single strongest decision-driving reason
- **隔离状态:** `INDEPENDENT_MODULES` or `REDUCED_ISOLATION_SINGLE_CONTEXT`
- **边界执行方式:** host-enforced or instruction-based; state the recorded context boundary
- **审核边界:** unreadable material, unavailable sources, genre constraints, or other unknowns

## 2. 最强拒稿理由

State the exact locator, failed condition, material consequence, strongest defence or fallback, why it fails or succeeds, detection confidence, and severity confidence.

## 3. Gate table

| Gate | Result | Decisive evidence | Consequence |
|---|---|---|---|
| Object/problem/RQ | PASS / MAJOR / BLOCK / UNKNOWN | exact locator | short consequence |
| Field/literature home | ... | ... | ... |
| Gap/contribution | ... | ... | ... |
| Claim/source relations | ... | ... | ... |
| Method/inference | ... | ... | ... |
| Access/ethics/timeline | ... | ... | ... |
| Programme/genre fit | ... | ... | ... |

## 4. Rejection-level findings

For each finding use:

### F[n] — concise issue name

- **Severity:** CRITICAL / MAJOR / MINOR / UNKNOWN
- **Module:** S1 / S2 / S3 / S4 / S5
- **Proposal evidence:** exact page, section, paragraph, table, or quotation fragment
- **Observed:** what the artifact actually says
- **Failed condition:** what must be true but is not established
- **Consequence:** what claim, inference, contribution, or feasibility judgement breaks
- **Strongest defence/fallback:** the best non-charitable rescue supported by available evidence
- **Residual problem:** why the defence fails, or what remains after it succeeds
- **Detection confidence:** high / medium / low
- **Severity confidence:** high / medium / low
- **Decision test:** the minimum new evidence or change that would clear or downgrade the finding

## 5. Cross-module adjudication

List duplicate findings merged, contradictions resolved, PASS counter-tests, and any proposed BLOCK that was downgraded after a credible fallback.

## 6. 优点（不抵消前述问题）

Report only strengths supported by the submitted artifact. Do not use them to soften the frozen verdict.

## 7. 修改优先级

Give no more than three ordered repairs unless the user requests a full revision plan:

1. change needed to clear the strongest decision blocker;
2. change needed to make the core inference or contribution defensible;
3. remaining high-value improvement.

For each repair, state what evidence would demonstrate success. Do not silently rewrite the proposal.

## 8. 下一步

Answer plainly:

- 现在是否建议送出？
- 最先必须解决什么？
- 如果通过，本机制的通过意味着什么、不意味着什么？

For calibration runs, append a separate post-freeze table with each human concern, `FULL/PARTIAL/MISS/CONTRADICTED`, severity comparison, and false-reassurance result.

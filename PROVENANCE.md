# Provenance and attribution

## Local source

Blind RP Review was adapted on 2026-10-03 from the locally maintained `stress-test-phd-rp` skill. The public preview is maintained by [Lllinkovo](https://github.com/Lllinkovo). The source snapshot and per-file hashes are retained in the private preparation log.

The candidate preserves the four specialist scopes, adjudication criteria, finding schema, and severity rules. Changes include a standalone entrypoint, explicit context-boundary reporting, proposal/S0 verification, consistent reduced-isolation handling, safer sidecar creation, mechanical tests, and synthetic evaluation fixtures.

## ARS relationship

The source skill required selected review resources from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills), through a local Codex adapter. The adapter manifest identifies source commit `828ef3b613b0e8b91830da3328a1e33d4eb5ab4c`.

Upstream author: **Cheng-I Wu (Imbad0202)**. Upstream license: **Creative Commons Attribution-NonCommercial 4.0 International**, verified at the pinned [LICENSE](https://github.com/Imbad0202/academic-research-skills/blob/828ef3b613b0e8b91830da3328a1e33d4eb5ab4c/LICENSE). The original copyright, license text, and warranty disclaimer are preserved in [LICENSES/ARS-CC-BY-NC-4.0.txt](LICENSES/ARS-CC-BY-NC-4.0.txt).

The local prototype explicitly used these upstream review resources:

- `academic-paper-reviewer/SKILL.md` (named `WORKFLOW.md` in the local adapter).
- `academic-paper-reviewer/agents/devils_advocate_reviewer_agent.md`.
- `academic-paper-reviewer/references/review_quality_thinking.md`.

The retained protocol reflects upstream review concepts, including evidence-to-claim checks, internal/external validity, contribution as a knowledge difference, strongest counterarguments, and field-norm severity calibration. We credit these contributions rather than presenting the complete review method as exclusively original.

This is a modified, standalone proposal-review workflow. It reorganizes the review into S0-S5, adds explicit context/input boundaries and file seals, defines proposal-specific severity and fallback rules, and supplies synthetic fixtures and CLI tests. The upstream suite itself is not bundled or required at runtime. This adaptation is not endorsed by the upstream author.

The preview is distributed under **CC BY-NC 4.0**, including the adaptation. Attribution, a license link, and modification notices must be preserved when applicable. See [LICENSE](LICENSE). The upstream warranty disclaimer is retained in the bundled license text.

## Materials

The three evaluation proposals and expectation records were written for this candidate and describe fictional studies. They contain no applicant manuscripts, real correspondence, or claimed empirical results.

# Blind RP Review

**Turn a PhD research proposal into a review with evidence, counterarguments, and ordered repairs.**

A reusable Agent skill for PhD applicants and researchers. Four specialists examine the **research question, literature contribution, claim–source relationships, and methods**. An adjudicator resolves disagreements after their reports are frozen.

[中文](README.md) · [Actual run and full reports](docs/DEMO.md) · [Quick start](#quick-start) · [Project presentation](docs/PROJECT_COPY.md)

## What you get

| Input | Process | Output |
|---|---|---|
| One fixed proposal or concept note | S0 scope/version record → S1–S4 specialist reviews → seal verification → S5 adjudication | Verdict, exact evidence locations, strongest counterarguments, resolution criteria, and up to three prioritized repairs |

The proposal stays unchanged. Keep previous human feedback separate until the verdict is frozen.

**[See the actual demonstration →](docs/DEMO.md)**  
The demonstration uses a fictional diagnostic excerpt and preserves the role outputs and verification record. It shows the output of this workflow; one example cannot establish general review accuracy. Reports are in Chinese, with an English overview in the demonstration guide.

## Why it exists

After several rounds of AI-assisted writing, the conversation contains explanations and accepted judgments that may never have reached the proposal itself. A reader sees the submitted text.

This workflow gives specialists fresh contexts and scoped inputs so they must establish their findings from that text and the permitted evidence.

## Design choices

| Mechanism | Problem addressed | Inspectable result |
|---|---|---|
| Fresh contexts and explicit inputs | Earlier feedback can influence a new review | Declared inputs and isolation method |
| Four specialist scopes | Broad feedback can hide where an argument fails | Located findings about questions, contribution, sources, and inference |
| Strongest-defence test | A serious-looking concern may have a credible fallback | Defence, residual problem, and calibrated severity |
| Frozen reports and file seals | Changing a draft mid-review can invalidate conclusions | SHA-256 and byte counts tied to the reviewed version |
| Evidence-based adjudication | Votes cannot resolve a substantive contradiction | Explained disagreements and acceptance criteria for repairs |

These are implemented workflow constraints. Superiority over another review method requires a separate controlled comparison.

## Quick start

### 1. Requirements

- An Agent host that reads local files and runs Python. The published demonstration uses Codex desktop.
- Python 3.10+; the seal script uses only the standard library.
- Full mode needs child contexts that inherit **no parent conversation**. Without them, the workflow declares reduced isolation from the start.
- PDF/Word extraction is supplied by the host. Use the Markdown fixture for a first trial.

This repository supplies skill instructions, role specifications, and a sealing script. Model execution, role scheduling, document parsing, and any model charges are supplied by your host.

### 2. Install in Codex

Windows PowerShell:

```powershell
git clone https://github.com/Lllinkovo/blind-rp-review.git "$HOME/.agents/skills/stress-test-phd-rp"
```

macOS / Linux:

```bash
git clone https://github.com/Lllinkovo/blind-rp-review.git "$HOME/.agents/skills/stress-test-phd-rp"
```

This uses the user-level discovery directory in the current [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills). Start a new session and select `$stress-test-phd-rp`; restart Codex if discovery has not updated. Compare an existing installation before replacing it.

Other hosts require their own skill discovery and child-context setup. This demonstration establishes behavior only in the recorded Codex environment.

### 3. Request a review

Replace `proposal.md` with your proposal path:

```text
Use $stress-test-phd-rp to review proposal.md.
Keep the proposal unchanged. Use fresh specialist contexts without parent
history and only their declared inputs. Check host support first and record
the actual isolation mode. Freeze the verdict before giving exact evidence,
the strongest counterargument, and up to three prioritized repairs.
Save reports and seals in a separate run directory.
```

To rerun the public example, use `examples/case-01/proposal.md` inside the installation. Do not give reviewers the published reports or `evals/expected.json`; a context that has seen the answers must be replaced.

## Workflow and outputs

```text
Proposal → S0 scope and version record
              ├─ S1 object, question, field
              ├─ S2 literature, gap, contribution
              ├─ S3 claims and sources
              └─ S4 methods, inference, access
                       ↓ freeze reports and reverify inputs
                   S5 adjudication
                       ↓
           verdict + findings + prioritized repairs
                       ↓ optional
              comparison with human feedback
```

| Verdict | Meaning |
|---|---|
| BLOCK | A demonstrated central failure survives the strongest supported defence |
| MAJOR REVISION | Material weaknesses remain, with a credible repair preserving the project |
| PASS FOR HUMAN REVIEW | No critical or major defect remains within this bounded review |

A run normally produces `S0_MANIFEST.md`, `S1_REPORT.md` through `S5_REPORT.md`, local seals, and a separate dispatch log. Findings include locators, evidence, consequences, counterarguments, confidence, and conditions for resolution. See the [output schema](references/output-schema.md).

## What “blind” means

Prior feedback, expected answers, and parent history are withheld. Author identities are not automatically anonymized. Fresh contexts can still share model biases. Instruction-based input restrictions are declared as such; file hashes establish byte consistency only.

Hosts without fresh contexts use `REDUCED_ISOLATION_SINGLE_CONTEXT`. A breach in a run claiming independence produces `RUN_INVALID_ISOLATION_FAILURE` and requires rerunning affected work.

## Validation and maintenance

- **12 seal CLI tests pass**, covering edits, path changes, malformed records, and overwrite protection.
- See the [actual run](docs/DEMO.md) and [validation record](docs/VALIDATION.md) for observed behavior and remaining evaluation.
- The [evaluation guide](docs/EVALUATION.md) describes three fictional fixtures. Once used to guide revisions, a public fixture is a regression case; generalization needs new cases.

```bash
python -B -m unittest discover -s tests -v
```

Report misses or unsupported findings through [Issues](https://github.com/Lllinkovo/blind-rp-review/issues), including an anonymized minimal input, host/isolation mode, relevant report excerpts, and evidence for the alternative judgment. Changes should include reproduction steps and before/after results. Keep private proposals, correspondence, credentials, and absolute-path seal sidecars out of public submissions.

## Contribution and attribution

Maintained by [Lllinkovo](https://github.com/Lllinkovo). This project translates a practical proposal-review need into S0–S5 roles, explicit input boundaries, frozen reports, Python version checks, fixtures, and tests.

The prototype drew on Cheng-I Wu’s [academic-research-skills](https://github.com/Imbad0202/academic-research-skills). This adaptation organizes relevant review concepts into a standalone proposal-review workflow. See [PROVENANCE.md](PROVENANCE.md) for the source and changes. Distributed under **[CC BY-NC 4.0](LICENSE)**.

[Project and interview copy](docs/PROJECT_COPY.md) · [Release scope and next steps](docs/RELEASE_REVIEW.md)

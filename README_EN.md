# Blind RP Review

**Put the key claims in your research proposal to the test.**

A multi-agent skill for reviewing PhD research proposals. Four specialist roles examine the research question, contribution, source support, and methods. An adjudicator then resolves disagreements against frozen reports and returns located findings with prioritized repairs.

[中文介绍](README.md) · [Evaluation](docs/EVALUATION.md) · [Validation status](docs/VALIDATION.md)

## Why it exists

After several rounds of writing with an AI assistant, the conversation contains explanations, accepted judgments, and reasons for earlier revisions. A review in that same context may rely on information a reader cannot find in the submitted text.

Blind RP Review withholds that history from its specialist reviewers. Each role must establish its findings from the selected proposal and permitted evidence. Prior human feedback becomes available only after the review is frozen.

## What the workflow provides

- **Fresh review contexts.** In full mode, specialists receive scoped inputs without the parent conversation, earlier reviews, or expected answers.
- **Four focused audits.** Question, contribution, sources, and methods are examined separately before the adjudicator handles overlap and disagreement.
- **A defence test for critical findings.** A blocking judgment needs an exact locator, a material consequence, and an explanation of why the strongest supported defence fails. A credible fallback can lower severity.
- **Version-specific conclusions.** File seals are checked before adjudication. Changed inputs invalidate affected downstream results until the new version is reviewed.
- **Repairs with acceptance criteria.** Important findings state what evidence or change would clear them. The final report recommends up to three ordered repairs.

## When to use it

Review a completed proposal, reassess a draft after extensive AI-assisted editing, compare a frozen review with human feedback, or check whether a revision resolves earlier findings.

“Blind” refers to withheld prior feedback and conversation history. It does not imply author anonymization or statistically independent model judgments. Record whether file access restrictions are host-enforced or instruction-based.

## Try it

Clone the repository into your host's skill directory using the local folder name `stress-test-phd-rp`. Start a new session and confirm discovery. Compare an existing installation before replacing it.

```text
git clone https://github.com/Lllinkovo/blind-rp-review.git stress-test-phd-rp
```

```text
Use $stress-test-phd-rp to review proposal.md.
Keep the proposal unchanged. Use fresh contexts without parent history.
Give the strongest defensible objection, exact evidence, its strongest
counterargument, and prioritized repairs.
```

Requires a file-capable agent and Python 3.10+ for report seals. Independent mode requires fresh child contexts; a single-context run must declare reduced isolation. Document extraction and model processing are supplied by the host.

The skill does not include an autonomous agent runner. It supplies instructions, scoped role specifications, an output schema, and a standard-library file-sealing tool.

## Check the package

```text
python -B -m unittest discover -s tests -v
```

[Evaluation cases](docs/EVALUATION.md) are synthetic fixtures, with expected findings held separately. Script tests do not measure academic review accuracy.

This is an **experimental preview**. All 12 seal CLI tests pass. Fresh-context behavioral trials and comparative academic evaluation remain pending. The official skill validator could not run because PyYAML is missing; basic structure and local links were checked separately.

## Attribution and license

The prototype drew on Cheng-I Wu's [academic-research-skills](https://github.com/Imbad0202/academic-research-skills). This standalone adaptation preserves attribution and describes the changes in [PROVENANCE.md](PROVENANCE.md). It is distributed under [CC BY-NC 4.0](LICENSE). See [release scope and next steps](docs/RELEASE_REVIEW.md).

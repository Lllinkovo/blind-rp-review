# 实际运行示例：从概念稿到冻结裁决

**这是一次真实执行的 Agent 审查，输入是虚构的研究设计片段。**  
日期：2026-10-04。最终结论：**BLOCK**。范围：只审查 C1 声明的因果主张与推断设计。

[查看输入](../examples/case-01/proposal.md) · [下载五份原始报告与校验清单](demo-reports.zip) · [跳到完整最终报告](#final-report) · [返回首页](../README.md)

## 一分钟看懂

输入想回答：**音频导览是否比纸质导览更能提高参观者第二天对展览事实的记忆？**

但它让周一的艺术史进阶班使用音频，让周六的首次访客使用纸本；没有基线资料或其他识别依据，却计划用两组分数的显著差异确立因果效果。

最终报告指出：即使两组分数不同，也无法从现有设计区分导览形式、访客背景和活动条件的作用。统一文本内容没有消除这个问题。输入又明确排除了“只描述这两组差异”作为中心答案，因此保留 BLOCK。

报告最后给出两项修复任务：先补足可执行的因果识别路径，再让分析与贡献表述对应这条路径。原稿没有被修改。

## 各角色实际产出了什么

| 阶段 | 观察到的输出 | 最终如何处理 |
|---|---|---|
| S1 问题与对象 | 问题清楚，比较结构与目标未对齐；局部 MAJOR | 保留问题清晰的判断，把错位并入核心识别问题 |
| S2 文献与贡献 | 因果贡献的归属缺少支持；局部 MAJOR；文献缺口 UNKNOWN | 贡献与方法属于同一推理链，不重复计数 |
| S3 主张与来源 | 未提供来源，来源支持 UNKNOWN | 没有虚构引用，也没有额外给出来源型拒稿理由 |
| S4 方法与推断 | 格式与群体／活动完全绑定；局部 BLOCK | 检验同文本辩护与描述性回退后仍保留 |
| S5 裁决 | 合并为一个核心发现，解释严重度差异，给出两项修复 | 冻结整体 BLOCK；不按票数或平均分决定 |

这张表是协调者在 S5 冻结后整理的阅读摘要。下面的最终报告和下载包保留模型原始输出；没有为了贴合预期答案而重写裁决。

## 运行与证据记录

- **宿主：** Codex desktop；Python 3.12 执行文件校验。宿主记录未提供可核实的具体模型标识，因此不声称使用了不同模型。
- **上下文：** S1、S2、S3、S4、S5 分别以 `fork_turns="none"` 派发，依次完成。专项角色不接收其他专项报告；S5 在四份报告冻结后才读取它们。
- **文件边界：** instruction-based 输入清单。各角色声明未发生已知越界；没有独立文件沙箱或完整文件访问审计。
- **S0 范围：** 189 词的虚构诊断片段，四节全部可读；未给项目要求，不允许外部浏览。中性映射为 P1 问题与贡献、P2 分组设计、P3 分析、P4 答案范围。
- **输入版本：** 1,270 字节；SHA-256 `221A1DC6257DEF46A8E094D1BF9A0E6FE08474C3E8B86159D7008D9643430230`。
- **封存顺序：** proposal 与 S0 先封存；S1–S4 各自完成后封存；协调者在 S5 前重新核验六项输入，S5 又复核了六项；S5 完成后封存并核验。七份材料最终均匹配。
- **最终报告：** 11,928 字节；SHA-256 `4C6BDA1410CA2B30AF3CBA68A6288682001BE70C7D05FD512104372EAB04FBFB`。
- **下载包：** 五份独立 Markdown 报告保持原始字节；`manifest.json` 记录输入和报告摘要、九个运行规则／脚本文件的版本摘要与派发方式。压缩包完整性及五份报告摘要已核对。含本机绝对路径的原始 S0、sidecar 和准备日志未公开。
- **评估状态：** 未把 `evals/expected.json` 交给审查者，也没有在本次演示后进行预期标签评分。C2、C3、重复试验与匹配基线对照仍未完成。

## 如何复现

按 [首页安装步骤](../README.md#快速开始) 安装，在新会话中将审查输入设为安装目录里的 `examples/case-01/proposal.md`。审查角色只接收 skill 声明的输入；不要把本页、下载报告或预期答案交给它们。

为新运行建立新的 S0、报告和校验记录。模型输出可能变化；应检查输入边界、证据链、裁决依据和文件一致性。需要衡量泛化表现时，使用没有公开答案的新案例。

## English overview

This is an actual Codex desktop run on a fictional 189-word diagnostic excerpt. Five fresh role contexts reviewed a fixed input, with instruction-based file restrictions. The final verdict was BLOCK: guide format was confounded with visitor group and event, and the submitted design supplied no other identifying evidence. The adjudicator merged overlapping findings and retained source support as UNKNOWN.

The full Chinese adjudication follows. The [download](demo-reports.zip) contains all five unedited reports and a portable manifest with hashes. One demonstration does not estimate accuracy or establish superiority over another method; no expected-label scoring or matched comparison was performed.

<a id="final-report"></a>

## 完整最终报告

以下保留冻结报告原文，方便核对结论、反驳、分歧处理和修改标准。

---

# S5 — 盲审最终裁决（冻结稿）

## 1. 审核结论

- **Verdict:** `BLOCK`
- **一句话理由：** 导览形式与访客群体、活动日期完全绑定，且没有其他识别证据；现有比较无法支持 P1 承诺的形式因果效应，P4 又明确排除描述性差异作为中心答案。
- **隔离状态：** `INDEPENDENT_MODULES`。
- **边界执行方式：** instruction-based。`run/DISPATCH.md` 记录 S1–S4 依次在 `fork_turns="none"` 的新上下文完成并封存，协调者核验六项输入后才派发 S5；本角色同样使用无父级历史的新上下文。该记录支持所声明的上下文边界，不构成完整文件访问审计或模型独立性证明；无模型多样性主张。
- **审核边界：** 189 词虚构诊断片段 C1，四节全部可读，仅裁决所述因果主张与推断设计。无参考文献、外查权限或项目要求；不据此判断完整博士申请的文献、伦理、准入或时间安排。
- **冻结声明：** 以下结论与最强拒稿理由在列出优点和修改建议前确定。裁决依据封存专项报告与提案原文，不按票数或平均严重度决定。

### 实际读取、封存与边界记录

便携标签：`package/` 指发布包；`run/` 指本次 `demo-2026-10-04-v1` 运行目录。

实际读取仅为：

- `package/examples/case-01/proposal.md`；`run/proposal.seal.json`。
- `run/S0_MANIFEST.md`；`run/S0_MANIFEST.seal.json`。
- `package/references/review-protocol.md`；`package/references/output-schema.md`；`package/references/modules/s5-adjudicator.md`。
- `run/S1_REPORT.md`、`run/S2_REPORT.md`、`run/S3_REPORT.md`、`run/S4_REPORT.md` 及各自同名的 `.seal.json` 文件。
- `run/DISPATCH.md`。

仅执行 `package/scripts/seal_report.py` 的帮助与 `--verify-sidecar` 功能，使用派发指定的 Python；未把脚本源码作为证据。S5 复核结果如下，各项均返回 `expected_match: true`，退出码为 0，路径、字节数与摘要均匹配：

| 输入 | 字节数 | SHA-256 |
|---|---:|---|
| proposal.md | 1270 | `221A1DC6257DEF46A8E094D1BF9A0E6FE08474C3E8B86159D7008D9643430230` |
| S0_MANIFEST.md | 6880 | `095E4995CBFD52193FAA7C707B1BDAD1CB02223D4946F2C60B35550B047A4F0F` |
| S1_REPORT.md | 6558 | `9E43F77AC3CA4E75744C460F44557D25BF89766C43ED7551315C13BD74D9B9D0` |
| S2_REPORT.md | 7308 | `B578641CE08D8550708935E401D717EB6820C42516C0A80E3C16E2DAEE5696CA` |
| S3_REPORT.md | 5794 | `C97E12F0ED57CA3264D9E2B55641598022CBA0265FC0AD1867CD97D9FBC0D5CE` |
| S4_REPORT.md | 6445 | `4981D7234D47FEC47B6DA3691A16E1B555794DE7FE7F4442769C0244806D5CA6` |

封存只证明字节与记录一致，不证明报告正确或独立性。**已知边界违规：无。** 未使用记忆、目录发现、其他文件、预期答案、人类反馈、浏览、外部服务或子代理；未开展新的专项审核，未修改输入。S0 中列出的其他角色规范未被打开。未发现需触发 `RUN_INVALID_ISOLATION_FAILURE` 的输入、顺序或边界失败。

## 2. 最强拒稿理由

**定位：** `proposal.md` P1 两句、P2 第 1 段、P3 第 1 段、P4 两句；对应 S4 F1，并与 S1 F1、S2 F1 同源。

**失败条件：** 要把均值差归于导览形式，所述证据必须能区分形式与访客群体／活动条件。P2 中音频只出现在周一进阶班，纸本只出现在周六首次访客活动；无基线知识或参与者特征，分配不可改变。P3 明示没有其他识别证据或调整，却将显著差异当作因果效应的成立依据。

**实质后果：** 即使形式没有效果，既有知识或活动条件也可能生成组间差异。这里没有断言这些替代解释已经发生；问题在于当前资料无法区分它们与形式效应。因此研究后可以直接得到两组得分差，却不能兑现 P1 要求的因果知识增量。显著、非显著或混合结果均不跨越该断点。

**最强辩护及裁定：** 文本相同、人数相同和统一的次日结果保留了比较基础；但不拆开形式、群体与活动。描述性结果可保留局部经验价值，但 P4 明确说它不回答中心问题。新识别设计可能保留原问题，不过 P2 锁定分配、P3 排除其他识别依据，P4 说明未提出设计修订；不能把尚未提供的设计当作当前可信的范围内救济。故保留 BLOCK，而非以可想象的未来修复降为 MAJOR。

**检测置信度：high；严重度置信度：high。** 判断依赖正文的因果目标与证据结构，不依赖未经核实的学科惯例。

## 3. Gate table

| Gate | Result | Decisive evidence | Consequence |
|---|---|---|---|
| Object/problem/RQ | PASS（仅清晰性） | P1 指明媒介对照、次日事实记忆；P4 明确答案标准；S1 | 问题可辨，不代表设计能回答 |
| Field/literature home | UNKNOWN | P1–P4 无文献定位；S1、S2 | 无法确认文献归属，不处罚诊断片段 |
| Gap/contribution | BLOCK（因果贡献）；文献缺口 UNKNOWN | P1、P3 的贡献承诺与 P2、P4 冲突；S2 F1、S4 F1 | 因果知识增量不成立；与方法项合并计为 F1 |
| Claim/source relations | UNKNOWN | 无引文及文献表；S3 | 外部支持不可核验，无独立来源误引发现 |
| Method/inference | BLOCK | P2–P3；S4 F1 | 两组检验无法单独识别形式效应 |
| Access/ethics/timeline | UNKNOWN | P2 仅说明两个活动；S4 | 不推断完整实施条件 |
| Programme/genre fit | PASS（诊断体裁）；项目适配 UNKNOWN | 开头体裁说明及 S0；S1 | 按片段范围审核，未评完整申请适配 |

## 4. Rejection-level findings

### F1 — 形式与群体活动绑定，核心因果贡献无法识别

- **Severity:** CRITICAL / BLOCK。
- **Module:** S4 F1 为识别依据；合并 S1 F1 的比较错位与 S2 F1 的贡献归属断点；S5 裁决。
- **Proposal evidence:** P1 “distinct from differences between visitor groups”；P2 “class receives audio guides”与“public-event group receives printed guides”，以及未收集特征、分配不可变的陈述；P3 “statistically significant difference will establish the causal effect”及无其他识别证据；P4 “descriptive difference ... would not answer”。
- **Observed:** `OBSERVED`：两场不同群体活动各使用一种格式；作者承诺因果贡献并排除描述性替代。`INFERRED`：所列比较无法将格式作用与群体／活动条件分离。
- **Failed condition:** 缺乏把观察差异归于形式的识别依据；统计显著性没有补足这一条件。
- **Consequence:** 比较结构错位 → 因果归属失败 → P1 知识增量无法兑现。这是一个缺陷的连续后果，不是三个独立拒稿理由。
- **Strongest defence/fallback:** 内容、人数和结果相同；检验可评价两组得分差；可退回描述性结果。
- **Residual problem:** 共同条件不建立群体可比性；描述性回退改变 P1/P4 的中心贡献。扩大原分配下的样本、追求更小 p 值或仅加入回归，均不在当前数据中生成格式与活动相区分的对照。未来重新设计尚未提交，不能充作现有方案的救济。
- **Detection confidence:** high。
- **Severity confidence:** high。
- **Decision test:** 提交可执行、可核查的识别设计或独立证据，说明如何区分形式、群体与活动效应，并把分析和贡献对应到该证据。若作者选择描述性问题，须明确变更中心后重新审核，不能视作原因果问题已经解决。

本项满足 BLOCK 的六项保留条件：精确定位、失败条件、中心后果、最强辩护、无法保留中心的理由、分开的两种置信度。未另列文献缺失、访问或伦理型拒稿项。

## 5. Cross-module adjudication

### 合并与分歧裁决

1. **S1 MAJOR、S2 MAJOR 与 S4 BLOCK：** 三份报告认可同一证据断点。S1、S2 的严重度均限定在专项范围，明确将识别失败与整体不可救济性留待 S4/S5。因此不是两份 MAJOR 抵消一份 BLOCK。依据 P2–P4 与 S4 的反证，合并 F1 并保留 CRITICAL/BLOCK。
2. **S1 的问题／范围 PASS 与 S4 BLOCK：** 前者确认对象、结果与答案边界清楚；后者判断设计不能兑现该答案。二者可同时成立。保留有范围限定的 PASS。
3. **S3 UNKNOWN 与 S4 BLOCK：** S3 判断外部来源支持不可核验；S4 从设计陈述判断因果识别失败。来源 UNKNOWN 不等于方法也只能 UNKNOWN，也不计为额外拒稿理由。
4. **其他未评估／UNKNOWN：** S1 对方法的移交、各模块对职责外项目的未评估，不与 S4 的已审核结论冲突。文献新颖性、项目适配与完整实施条件继续 UNKNOWN。
5. **BLOCK 降级测试：** 同文本辩护和描述性回退均不能保留已声明的中心贡献，未降级。没有其他拟议 BLOCK。无实际证据支持另一项相反结论。

### 每个保留 PASS 的两项反测

S1 的对象、RQ、范围与诊断体裁四项局部 PASS 均保留；未将其扩为整体通过。

| 局部 PASS | 反测 1：证据与结果 | 反测 2：证据与结果 |
|---|---|---|
| 对象清晰 | 是否从记忆转成满意度？P1/P3 一直指向事实记忆及测验得分，未发现对象替换 | 是否从个人结果跳到机构效益？P1–P4 无该主张；通过该清晰性测试 |
| RQ／答案标准清晰 | 媒介和时间是否含糊？P1 明确音频／纸本与次日记忆；通过 | 描述性差异是否也被定义为充分答案？P4 明确排除；答案标准清楚，虽未被设计满足 |
| 声明范围清晰 | 是否声称长期或所有学习结果？P1 仅为次日事实记忆；无该扩张 | 是否承诺机制解释或跨场馆推广？P1–P4 未承诺；通过声明边界测试，外推有效性仍未获证明 |
| 诊断体裁适配 | 是否应因没有完整综述而判失败？开头与 S0 限定诊断摘录；无此体裁义务 | 片段标签是否使因果主张免审？P1/P3 仍有明确承重主张，本次以 F1 判 BLOCK；体裁适配不提供豁免 |

**有效性与文风核对：** 内部识别失败直接驱动裁决；外部／迁移有效性没有可核查支持，不另加缺陷。S2 所述“得分差 → 形式因果知识”的增量未实现。按 S1–S4 的相反文风测试，将 P3 换成技术或口语表达不改变分配结构与该结论。

## 6. 优点（不抵消前述问题）

P1 明确对照与结果；P2 公开内容和分配约束；P4 清楚划定因果问题与描述性答案的区别。这些陈述使关键缺陷可以准确定位，不提供有效因果识别的保证。

## 7. 修改优先级

1. **先补足识别路径。** 提交可执行的比较／分配设计或独立识别证据，解释如何区分格式与群体、活动效应。成功证据是具体安排、可检验假设及其与 P1 估计目标的对应；若现有限制下无法取得，应先由作者决定是否变更中心问题。
2. **使分析与贡献服从该识别路径。** 明确实际分配层级、检验承担的任务，以及各类结果能支持什么结论。成功证据是修订后的 P3 不再把显著性本身当作因果识别，并能说明如何从资料得到 P1 所要求的知识。

不为本诊断短篇增加完整综述、伦理或申请材料的修补任务；未改写提案。

## 8. 下一步

- **现在是否建议送出？** 不建议将当前片段作为能够支持所述因果贡献的研究设计送出。冻结结论为 BLOCK。
- **最先必须解决什么？** 格式与群体／活动效应无法区分的识别问题。
- **如果通过，本机制的通过意味着什么？** 未来通过仅表示限定输入与范围内未保留重大或阻断缺陷；不保证真实因果效应、完整申请质量、外部来源穷尽或录取结果。本次尚未通过。

本报告为盲审冻结稿，未读取人类反馈，未进行事后校准。
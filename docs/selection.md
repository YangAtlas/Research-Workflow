# Skills 选型说明

选型围绕一个具体目标：把已读论文转化为值得研究的问题，再把问题转化为能接受实验检验的假设。来源核实日期为 2026-09-26 至 2026-09-27。

## 1. 输入：保留清楚的阅读入口

| 场景 | 选择 | 理由 |
|---|---|---|
| Zotero 中的论文 | zotero-paper-reader，主力 | 连接条目、原文和研究库归档，保留证据位置 |
| Agentero 文献库 | 项目内 paper-reader | 与项目的文献和笔记约定衔接 |
| 独立 PDF 或论文链接 | paper-analyzer，按需 | 适合深入分析方法、公式、代码和实验 |

[OpenAI Zotero](https://github.com/openai/plugins/blob/main/plugins/zotero/skills/zotero/SKILL.md) 可补充本地查询、条目管理、BibTeX 导出和引用操作。当文献操作成为瓶颈时再引入。

[xmustu/zotero-obsidian-codex](https://github.com/xmustu/zotero-obsidian-codex) 将知识组织成论文、概念、综合和问题页；[parasurama/autolit](https://github.com/parasurama/autolit) 区分同步、单篇提炼和跨篇综合。两者的知识组织方式值得参考，接入时需要适配已有研究库和依赖。

## 2. 思考：优先补齐跨论文综合

**优先复用 Agentero 已有 deep-research 的主题综合方法。** [Supervisor 的 synthesis-framework](https://github.com/HKUSTDial/Supervisor-Skills/blob/main/skills/deep-research/references/synthesis-framework.md) 提供主要发现、方法、成立条件和论文间关系的组织方式。用它把一组已读笔记整理为：

**主要发现与条件 → 共识与分歧 → 候选解释 → 值得研究的问题 → 下一份关键证据。**

brainstorming-research-ideas 保留为主力，接在综合材料之后，用于类比、解释异常、寻找失败条件和提出候选方向。分类表中未覆盖的格子先视为当前材料的缺口；进一步检索后才能判断是否存在研究机会。

[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) 的 [json-canvas](https://github.com/kepano/obsidian-skills/blob/main/skills/json-canvas/SKILL.md) 可在研究库项目中按需加入，连接论文、概念、问题、假设和实验记录。画布帮助整理关系，问题是否值得投入仍需研究者判断。

## 3. 输出假设：明确解释、预测与证伪条件

clarify-research-idea 保留为主力，负责任务定义、研究定位、方法结构和假设收束。资源投入较大时，使用项目内 idea-evaluator 讨论相近工作、困难和可行性。

[K-Dense hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md) 的 2.2 版值得借鉴：区分观察、机制、假设和预测，提出竞争解释，并设计能区分解释的实验。先将这部分方法接入假设卡；需要经常独立调用时再引入完整 skill。

## 4. 验证：让结果改变下一步行动

academic-plotting 保留为数据图主力，drawio-skill 保留为可编辑结构图主力。图形分别服务于数值证据和方法关系的表达。

| GitHub 来源 | 适用判断 |
|---|---|
| [scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md) | 1.3 版侧重方法、混杂、偏差和证据边界，适合按需审视实验解释 |
| [scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) | 可参考数值图的证据组织和出版呈现；完整流程另有工具要求 |
| [Agents365 drawio-skill](https://github.com/Agents365-ai/drawio-skill) | 本包为 2.1.0，所读上游为 3.4.0；按系统结构、多视图等实际需求决定升级 |
| [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp/blob/main/plugins/codex/drawio/skills/drawio/SKILL.md) | 提供 XML/Mermaid 与图形导出，可作为另一实现来源 |

## 5. 输出成果：按成品选择工具

| 角色 | Skills | 分工 |
|---|---|---|
| 主力 | ml-paper-writing、systems-paper-writing | 按研究类型组织论文论点和证据 |
| 主力 | md-to-html | 将定稿 Markdown 发布为网页阅读版 |
| 按需 | humanizer、doc-coauthoring | 文字整理、研究方案和协作文档 |
| 按需 | academic-figure-prompt、paper-comic | 图像提示词、论文机制讲解 |
| 按需 | paper-deck、html-copy-studio | 逐页生图幻灯片、讲稿与视觉构思 |
| 备用 | canvas-design、docx | 通用视觉设计、Word 文档处理 |

[humanizer](https://github.com/blader/humanizer) 有明确的同源更新：本包为 2.9.1，所读上游为 3.0.0。可用同一段真实稿件比较事实保留、作者语气和文字清晰度后决定更新。

[paper-craft-skills](https://github.com/zsyggg/paper-craft-skills) 是 paper-analyzer、paper-comic 和 paper-deck 的上游来源。本包保留本地的 Markdown 主稿与按需 HTML 发布流程。

需要可编辑文字和图元的幻灯片时使用 presentations；Word 常规任务可用 documents。canvas-design 适合通用设计需求，docx 的获取方式见其简介。

## 6. 常用集合与迭代方式

共 17 个个人 skills：

- **8 个主力**：zotero-paper-reader、brainstorming-research-ideas、clarify-research-idea、academic-plotting、drawio-skill、ml-paper-writing、systems-paper-writing、md-to-html。
- **7 个按需**：paper-analyzer、humanizer、academic-figure-prompt、paper-comic、paper-deck、html-copy-studio、doc-coauthoring。
- **2 个备用**：canvas-design、docx。

这些角色用于选择入口。需要调整调用频率时，再修改相应 skill 的触发描述或宿主设置。升级同类工具时，用一项真实任务判断它是否改善了当前问题：阅读看来源可追溯性，综合看研究问题是否明确，假设看实验能否区分解释，图形看数据和关系是否准确，写作看主张是否有证据。

## 已知问题与来源范围

- 现有 paper-analyzer 包含固定内容数量要求，clarify 包含评分步骤，ml-paper-writing 存在需要统一的写作确认条件。使用时以实际材料、研究者判断和已经给出的授权为准，后续可分别精简对应指令。
- academic-plotting 同时包含数据图与 Gemini 生图流程，存在配色、后端和生成次数的适配需求；drawio 的触发范围较宽。按前述图形分工选择调用入口。
- md-to-html 的公式和 Mermaid 默认依赖 CDN，需要离线阅读时应准备对应运行库。
- 本地四项 Orchestra 技能的 SKILL 正文与所读上游一致，比较提交为 `773a52944ba4747a18bd4ae9ade53fff041adcbc`。K-Dense 比较提交为 `49c6e97775eaa18ba791bebe23162a70ae601c18`。这些记录用于定位来源版本。
- K-Dense 的 scientific-brainstorming 更偏团队讨论；literature-review 包含额外认证和工具流程，适合专门开展相应任务时考察。其技能正文另有实际使用后的项目论文引用要求。
- 源码比较用于判断方法和依赖，运行效果需要真实任务验证。第三方许可及待确认事项见 [来源与许可](sources-and-licenses.md)。

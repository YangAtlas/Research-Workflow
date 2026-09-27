# Research Workflow

用 Zotero、Agentero、Obsidian 与 Codex 串起科研中的阅读、思考、假设、实验和表达。

这个仓库整理一套可以持续使用和迭代的科研流程，以及各环节的 skills、安装包和记录模板。重点是让阅读积累逐渐形成自己的研究问题，并让研究判断接受实验检验。

[直接查看 34 项 Skills 分类表与安装入口](#skills-overview)

```mermaid
flowchart LR
    A[输入：文献与研究现象] --> B[思考：综合证据与提出问题]
    B --> C[输出一：假设与研究方案]
    C --> D[验证：实验与证据判断]
    D --> E[输出二：论文与成果分享]
    D -->|修正解释| B
    D -->|调整实验| C
    E -->|新问题| A
```

## 1. 输入：收集、精读与积累

Zotero 管理文献与引用，Agentero 配合 Agent 阅读论文，Obsidian 保存可以继续编辑、关联和综合的研究笔记。

精读之后应留下：研究问题、主要结论、成立条件、关键方法、实验依据、局限，以及它与当前研究的关系。重要判断关联原文的章节、图表或代码位置。

| 入口 | 作用 | 交接成果 |
|---|---|---|
| Zotero → [zotero-paper-reader](catalog/zotero-paper-reader.md) | 定位条目与 PDF，精读并归档到研究库 | 有来源与审阅状态的论文笔记 |
| Agentero 项目内的 paper-reader | 结合文献库原文和已有笔记阅读 | 库内论文讲义 |
| 独立 PDF → [paper-analyzer](catalog/paper-analyzer.md) | 分析方法、公式、实验、代码和局限 | 可持续维护的 Markdown 主稿 |

每条笔记区分作者陈述、实验结果、AI 推断和研究者决定。论文的 DOI 通过出版商或可靠索引核实；尚未分配时保留稳定链接并明确说明。

## 2. 思考：从多篇论文形成研究问题

这一阶段围绕共同的问题组织材料，比较论文之间的共识、分歧和成立条件。

1. **聚合材料**：选取围绕同一现象、任务或机制的论文笔记。
2. **对齐条件**：比较输入信息、数据、假设、评价指标和资源条件。
3. **解释分歧**：定位不同结论是否来自不同条件，找出仍未被解释的现象。
4. **提出问题**：写清具体困难影响什么、已有解释到哪里、还缺什么证据。
5. **选择方向**：结合问题的重要性和可取得的数据，决定下一步投入。

| 能力 | 适用时机 |
|---|---|
| Agentero 的 deep-research | 系统调研与主题综合；[上游综合方法](https://github.com/HKUSTDial/Supervisor-Skills/blob/main/skills/deep-research/references/synthesis-framework.md) |
| [brainstorming-research-ideas](catalog/brainstorming-research-ideas.md) | 从矛盾、失败条件、类比或简化中提出候选解释 |
| [研究问题备忘录](templates/research-question.md) | 将阅读所得整理为候选问题、优先问题和下一份证据 |

这一阶段的主要成果是一页研究问题备忘录：已有证据、关键分歧、未解释现象、优先问题及理由。

## 3. 输出一：形成假设与研究方案

选定问题后，将它写成可检验的研究设想：任务是什么，核心假设是什么，若假设成立应观察到什么，以及什么结果会削弱或推翻它。

- [clarify-research-idea](catalog/clarify-research-idea.md)：明确任务、相近工作、方法结构、假设和验证线索。
- Agentero 的 idea-evaluator：在投入较多资源前讨论相近工作、关键困难与可行性。
- [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md)：可参考其竞争解释、不同预测和区分性实验设计。

使用 [假设卡](templates/hypothesis.md) 记录当前解释、竞争解释、预期观察和证伪条件。研究者决定选择哪个假设，以及投入多少时间和资源。

## 4. 验证：实验、证据与下一步决定

实验前明确这次运行要区分什么，以及不同结果将如何改变下一步行动。实验中记录配置、数据划分、比较方法与结果来源；实验后回到假设，判断证据支持到哪里。

| 工作 | 记录内容 |
|---|---|
| 实验设计 | 改变什么、固定什么、与谁比较、观察什么 |
| 数据与配置 | 训练、验证和测试的分工；用于选择设置的数据；最终冻结的配置 |
| 实验执行 | 运行环境、代码版本、输入、参数、原始结果与异常 |
| 证据判断 | 观察、解释、竞争解释、适用条件和下一步决定 |

[实验方案](templates/experiment-plan.md) 与 [证据结论](templates/evidence-summary.md) 承接这一阶段。数值图使用 [academic-plotting](catalog/academic-plotting.md)，精确的结构和关系图使用 [drawio-skill](catalog/drawio-skill.md)。

## 5. 输出二：论文、图表与成果分享

围绕证据组织论点，再根据受众选择表达形式。

| 成果 | 对应 skill |
|---|---|
| ML/AI 论文 | [ml-paper-writing](catalog/ml-paper-writing.md) |
| 系统论文 | [systems-paper-writing](catalog/systems-paper-writing.md) |
| 文字整理 | [humanizer](catalog/humanizer.md) |
| 学术图提示词 | [academic-figure-prompt](catalog/academic-figure-prompt.md) |
| 方法与机制图解 | [paper-comic](catalog/paper-comic.md) |
| 逐页生图幻灯片 | [paper-deck](catalog/paper-deck.md) |
| 演讲文案与视觉构思 | [html-copy-studio](catalog/html-copy-studio.md) |
| Markdown 网页阅读版 | [md-to-html](catalog/md-to-html.md) |
| 项目说明与协作文档 | [doc-coauthoring](catalog/doc-coauthoring.md) |
| 通用视觉设计 | [canvas-design](catalog/canvas-design.md) |
| Word 文档 | [docx 来源与使用说明](catalog/docx.md)；Codex 中也可使用 documents 插件 |

需要可编辑的幻灯片文字与图元时，可使用宿主提供的 presentations 能力。分享反馈形成的新问题继续进入阅读和思考环节。

## 工作约定与知识库

三层内容共同支撑这套流程：

- **全局约定**：来源核实、事实与推断区分、表达方式和验证范围。
- **项目约定**：资料位置、领域路由、实验命令、数据边界和成果归档。
- **Skills**：具体任务的可复用方法、脚本、模板和资源。

可从 [AGENTS.md 示例](config-examples/AGENTS.md) 开始，为自己的研究库补充目录和实验约定。不同机器的路径、外部模型服务和数据源在使用时配置。

个人、系统、插件与 Agentero 项目技能的职责见 [Skills 与工作约定的层次](docs/skill-layers.md)。

<a id="skills-overview"></a>

## Skills 总览：34 项

以下为整理时会话可用的 **34 个 skills：17 个个人、5 个系统、12 个插件**。按科研流程的主要用途分类，每项使用统一编号；一个 skill 可以参与多个阶段。

个人技能中，8 个建议作为主力、7 个按需使用、2 个备用，详见 [选型说明](docs/selection.md)。表中 ZIP 可直接下载；系统和插件技能通过对应宿主或插件提供。Agentero 的项目技能另见 [技能层次](docs/skill-layers.md)。

### 输入：文献阅读与材料提取

| 序号 | Skill | 来源 | 简介 | 安装 / 使用 |
|---|---|---|---|---|
| 01 | [zotero-paper-reader](catalog/zotero-paper-reader.md) | 个人 | 从 Zotero 定位论文和 PDF，精读后归档为有证据来源的研究笔记。 | [ZIP](packages/01-zotero-paper-reader.zip) |
| 02 | [paper-analyzer](catalog/paper-analyzer.md) | 个人 | 深入分析论文的方法、公式、实验、代码和局限，形成 Markdown 主稿。 | [ZIP](packages/02-paper-analyzer.zip) |
| 03 | `pdf` | 插件 | 读取、提取、创建和渲染 PDF，检查页面内容与排版。 | 对应插件提供 |

### 思考：研究问题与关系整理

| 序号 | Skill | 来源 | 简介 | 安装 / 使用 |
|---|---|---|---|---|
| 04 | [brainstorming-research-ideas](catalog/brainstorming-research-ideas.md) | 个人 | 借助类比、矛盾和失败条件，提出候选研究问题与探索方向。 | [ZIP](packages/04-brainstorming-research-ideas.zip) |
| 05 | `visualize` | 插件 | 用交互图解、模拟和对比工具帮助理解机制、条件变化与问题关系。 | 对应插件提供 |

### 输出一：假设与研究方案

| 序号 | Skill | 来源 | 简介 | 安装 / 使用 |
|---|---|---|---|---|
| 06 | [clarify-research-idea](catalog/clarify-research-idea.md) | 个人 | 将初步想法整理为任务定义、研究定位、核心假设、方法结构和验证线索。 | [ZIP](packages/06-clarify-research-idea.zip) |

### 验证：实验数据与图表

| 序号 | Skill | 来源 | 简介 | 安装 / 使用 |
|---|---|---|---|---|
| 07 | [academic-plotting](catalog/academic-plotting.md) | 个人 | 将实验数据绘制为论文数值图，也支持根据方法描述生成学术图形。 | [ZIP](packages/07-academic-plotting.zip) |
| 08 | [drawio-skill](catalog/drawio-skill.md) | 个人 | 制作可编辑的流程图、方法图和系统结构图，并导出图片或 PDF。 | [ZIP](packages/08-drawio-skill.zip) |
| 09 | `spreadsheets` | 插件 | 创建和分析表格文件，处理公式、统计汇总、图表与结果展示。 | 对应插件提供 |
| 10 | `excel-live-control` | 插件 | 通过连接的 Excel 会话操作当前工作簿，适合现场查看和整理实验数据。 | 对应插件提供 |

### 输出二：论文、文档与分享

| 序号 | Skill | 来源 | 简介 | 安装 / 使用 |
|---|---|---|---|---|
| 11 | [ml-paper-writing](catalog/ml-paper-writing.md) | 个人 | 组织 ML/AI 论文论点、结构、正文与引用，配合会议模板完成写作。 | [ZIP](packages/11-ml-paper-writing.zip) |
| 12 | [systems-paper-writing](catalog/systems-paper-writing.md) | 个人 | 围绕系统设计、实现和测量证据组织系统类论文及评价论证。 | [ZIP](packages/12-systems-paper-writing.zip) |
| 13 | [humanizer](catalog/humanizer.md) | 个人 | 整理已有文字中的模板化表达，保留事实、作者语气和自然行文。 | [ZIP](packages/13-humanizer.zip) |
| 14 | [academic-figure-prompt](catalog/academic-figure-prompt.md) | 个人 | 把论文内容和图形需求整理为可交给图像工具的详细英文提示词。 | [ZIP](packages/14-academic-figure-prompt.zip) |
| 15 | [paper-comic](catalog/paper-comic.md) | 个人 | 用方法概览和机制细节图解释论文的核心方法与工作过程。 | [ZIP](packages/15-paper-comic.zip) |
| 16 | [paper-deck](catalog/paper-deck.md) | 个人 | 设计逐页叙事与视觉方案，生成幻灯片图片并合成为 PPTX/PDF。 | [ZIP](packages/16-paper-deck.zip) |
| 17 | [html-copy-studio](catalog/html-copy-studio.md) | 个人 | 将逐页文案、讲稿和视觉构思整理成可审阅、可复制的 HTML 工作台。 | [ZIP](packages/17-html-copy-studio.zip) |
| 18 | [md-to-html](catalog/md-to-html.md) | 个人 | 将 Markdown 或 Obsidian 主稿发布为响应式 HTML 阅读版。 | [ZIP](packages/18-md-to-html.zip) |
| 19 | [doc-coauthoring](catalog/doc-coauthoring.md) | 个人 | 围绕受众、背景和目的共创研究方案、README 与项目说明文档。 | [ZIP](packages/19-doc-coauthoring.zip) |
| 20 | [canvas-design](catalog/canvas-design.md) | 个人 | 制作海报和静态视觉设计，输出 PNG/PDF 等成品。 | [ZIP](packages/20-canvas-design.zip) |
| 21 | [docx](catalog/docx.md) | 个人 | 创建、编辑和整理 Word 文档，支持模板、修订及批注等任务。 | [来源指引](catalog/docx.md) |
| 22 | `documents` | 插件 | 制作和编辑 Word 文档，通过渲染检查页面布局、内容与修订。 | 对应插件提供 |
| 23 | `presentations` | 插件 | 读取、创建和编辑 PowerPoint 或 Google Slides 演示文稿。 | 对应插件提供 |
| 24 | `imagegen` | 系统 | 根据描述生成图片，或编辑已有图片的内容、风格与背景。 | 系统提供 |
| 25 | `sites-building` | 插件 | 制作完整的网站、项目主页、仪表板或展示门户。 | 对应插件提供 |
| 26 | `sites-hosting` | 插件 | 通过 Sites 发布和更新网站，管理对应托管。 | 对应插件提供 |
| 27 | `sites-preview-troubleshooting` | 插件 | 诊断和恢复受支持环境中的 Sites 预览会话故障。 | 对应插件提供 |

### 通用支撑：工具操作与技能维护

| 序号 | Skill | 来源 | 简介 | 安装 / 使用 |
|---|---|---|---|---|
| 28 | `computer-use` | 插件 | 通过界面操作支持的应用与浏览器，承接需要交互操作的任务。 | 对应插件提供 |
| 29 | `openai-docs` | 系统 | 查阅 OpenAI 官方资料，处理 Codex、模型、设置和 API 的使用问题。 | 系统提供 |
| 30 | `skill-creator` | 系统 | 创建和更新 skill 的任务说明、触发条件及配套资源。 | 系统提供 |
| 31 | `skill-installer` | 系统 | 从精选目录或 GitHub 仓库路径安装 Codex skills。 | 系统提供 |
| 32 | `plugin-creator` | 系统 | 创建和维护 Codex 插件结构、清单与个人插件市场条目。 | 系统提供 |
| 33 | `plugin-management` | 插件 | 发现插件，查看权限和依赖，管理连接及移除。 | 对应插件提供 |
| 34 | `template-creator` | 插件 | 从参考文档、幻灯片、表格或设计中创建可复用的个人模板技能。 | 对应插件提供 |

安装包采用 `序号-skill名称.zip` 命名，与表格编号对应。解压后的目录使用 skill 名称，例如 `01-zotero-paper-reader.zip` 解压为 `zotero-paper-reader/`。

## 安装与使用

### 单个 ZIP 包

从 [安装包目录](packages/README.md) 下载所需 ZIP。解压后得到同名 skill 文件夹，包含 `SKILL.md` 和运行所需资源。

将该文件夹放到 Codex 的个人 skills 目录，或项目的 `.agents/skills/`。具体目录以当前宿主的技能设置为准。

### 使用仓库安装器

克隆或下载仓库后，使用 Python 3.10+：

```bash
python scripts/install_skill.py --list
python scripts/install_skill.py clarify-research-idea
python scripts/install_skill.py paper-comic --dest /path/to/project/.agents/skills
```

默认安装到 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。`--dest` 指定的是容纳多个 skills 的根目录。已有同名目录时安装器停止，保留现有版本。

安装后让 Codex 重新发现技能；未显示时重启会话。按 skill 名称调用，例如：

```text
使用 clarify-research-idea，基于我的研究问题备忘录，明确核心假设和最小验证方案。
```

Python 库、draw.io、Pandoc、图像服务等依赖见各技能简介。安装器负责安装 skill 文件；外部依赖按实际使用的工作流准备。

## 目录

```text
catalog/          34 项分类索引与 17 个个人技能详细简介
packages/         16 个完整 ZIP 安装包
docs/             工作流用法、选型与来源说明
templates/        研究问题、假设、实验和证据模板
config-examples/  研究协作约定示例
scripts/          本地安装器
```

## 来源、许可与已知限制

- 安装包来自本地维护版本，保留其上游说明与随附资源。每个包的 `SOURCE.md` 记录来源和本次打包说明。
- `docx` 采用来源索引形式，其现有许可限制再分发；获取方式见对应简介。
- 第三方内容遵循各自许可；本地维护内容的单独许可状态及待确认事项集中记录在 [来源与许可](docs/sources-and-licenses.md)。
- 本次验证覆盖安装包结构、资源保留、安装器和库路径解析。各科研技能的完整执行仍依赖对应资料、工具与服务。
- 仓库维护日期：2026-09-27。

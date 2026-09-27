# Skills 与工作约定的层次

一次科研任务会同时用到个人 skills、宿主提供的技能、项目技能和 AGENTS.md。把它们分开维护，有助于明确每项内容放在哪里。

## 个人技能

本仓库的 [17 个技能简介](../catalog/README.md) 对应个人长期维护的研究工具。其中 16 个附完整 ZIP；安装器可将选定技能放入个人目录或项目的 `.agents/skills/`。

## 系统与插件能力

整理时，会话另有 5 个系统技能：imagegen、openai-docs、plugin-creator、skill-creator、skill-installer。

插件提供 12 项技能：computer-use、documents、pdf、presentations、spreadsheets、excel-live-control、plugin-management、sites-building、sites-hosting、sites-preview-troubleshooting、template-creator、visualize。

这些能力随宿主或插件分发，安装和升级通过原发行渠道管理。常见分工是：PDF 读取、Word 和幻灯片制作、表格处理、交互演示、网页发布及工具维护。

## Agentero 项目技能

| 阶段 | 项目技能 | 职责 |
|---|---|---|
| 输入 | agentero-cli、paper-reader、equation-annotation、author-lookup | 文献库访问、精读、公式标注和作者信息核实 |
| 思考 | deep-research | 检索、综合与主题调研 |
| 输出假设 | idea-evaluator | 研究设想、相近工作与可行性讨论 |
| 验证与表达 | acdemic-drawing | 方法与系统图形；名称沿用项目实际目录 |
| 输出成果 | research-paper-writing | 项目中的论文写作流程 |
| 全流程 | vault-normalizer | 知识库整理与一致性维护 |

项目技能依赖对应知识库及工具配置，适合随项目管理。部分方法可参考 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)。

## 全局和项目 AGENTS.md

全局约定适合放入来源核实、文字风格、事实与推断的区分、验证范围等长期规则。

项目约定适合放入研究领域、资料位置、实验命令、数据边界和成果归档：文献库项目负责材料访问与阅读，研究笔记库负责领域和笔记路由，实验代码项目负责运行与结果记录。

[研究协作示例](../config-examples/AGENTS.md) 可作为起点。项目目录和服务配置由使用者补充，实际任务由所选 skill 承担具体步骤。

# zotero-paper-reader

Zotero 论文精读与研究库归档。

| 项目 | 说明 |
|---|---|
| 流程位置 | 输入 |
| 使用建议 | 主力 |
| 输入 | Zotero 条目、PDF 与目标研究库 |
| 输出 | 有来源、图表解读和审阅状态的中文 Markdown 笔记 |
| 依赖 | Python 3、PDF 提取与视觉读取；Zotero connector 或本地 Zotero 数据目录 |
| 来源 | 本地维护版本 |
| 许可 | 本地维护快照；原目录未单独声明许可证，上游来源与开放许可待维护者补充。 |
| 快照日期 | 2026-09-27 |

## 安装

[下载完整安装包](../packages/zotero-paper-reader.zip)

下载仓库后，也可运行：

```bash
python scripts/install_skill.py zotero-paper-reader
```

ZIP 的顶层目录是 `zotero-paper-reader/`，保留原技能的 SKILL.md、脚本、参考文件、模板和资源。完整文件清单可直接查看 ZIP 内容。

## 使用

在 Codex 中按名称选择 `zotero-paper-reader`，提供表中列出的输入，并说明期望成品。

## 研究库设置

使用前提供研究库根目录。路径解析脚本要求显式传入 `--vault`，领域可通过 `--area` 指定。默认目录结构和领域示例见包内 `references/vault-profile.md`。

[返回技能目录](README.md) · [科研流程](../README.md)

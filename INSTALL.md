# 安装与使用

本说明对应仓库中的三款 Codex v2 宠物。请使用支持自定义宠物的 Codex 版本；应用入口名称可能随版本变化，以下重点说明文件的放置方式。

## 1. 选择下载包

| 版本 | 下载 | 配置中的显示名 | 宠物 ID |
| --- | --- | --- | --- |
| 原版 | [amakawa-mamuko-v2.zip](downloads/amakawa-mamuko-v2.zip) | 天川真梦梓 | `amakawa-mamuko` |
| 通行证皮 | [mamuko-pass-v2.zip](downloads/mamuko-pass-v2.zip) | 真梦梓 通行证皮 | `mamuko-pass` |
| 羁绊 v2 | [amakawa-mamuko-bond-v2.zip](downloads/amakawa-mamuko-bond-v2.zip) | 天川真梦梓 羁绊v2 | `amakawa-mamuko-bond-v2` |

三款 ID 不同，可同时安装。ZIP 文件页中可以使用下载按钮保存；如果下载的是整个仓库，直接使用下文列出的安装文件夹。

## 2. 放到正确位置

默认目标是**当前用户主目录**下的 `.codex/pets/`。Windows 可在资源管理器地址栏输入 `%USERPROFILE%\.codex\pets`；目录不存在时先创建。macOS / Linux 对应 `~/.codex/pets/`。如果你的 Codex 已配置自定义用户目录，应使用该目录下的 `pets/`。

### 下载 ZIP 安装

- **原版**：ZIP 中的 `pet.json` 与 `spritesheet.webp` 解压到 `.codex/pets/amakawa-mamuko/`。
- **通行证皮**：先解压完整包，将其中 `mamuko-pass-v2/mamuko-pass/` 文件夹复制到 `.codex/pets/`。完整包外层的 `mamuko-pass-v2` 用于存放说明与预览。
- **羁绊 v2**：ZIP 中的 `pet.json` 与 `spritesheet.webp` 解压到 `.codex/pets/amakawa-mamuko-bond-v2/`。

### 下载整个仓库后安装

| 仓库内要复制的文件夹 | 安装后的文件夹 |
| --- | --- |
| `amakawa-mamuko/` | `.codex/pets/amakawa-mamuko/` |
| `mamuko-pass-v2/mamuko-pass/` | `.codex/pets/mamuko-pass/` |
| `mamuko-bond-v2/amakawa-mamuko-bond-v2/` | `.codex/pets/amakawa-mamuko-bond-v2/` |

正确层级如下；可只安装其中一款：

```text
.codex/
└── pets/
    ├── amakawa-mamuko/
    │   ├── pet.json
    │   └── spritesheet.webp
    ├── mamuko-pass/
    │   ├── pet.json
    │   └── spritesheet.webp
    └── amakawa-mamuko-bond-v2/
        ├── pet.json
        └── spritesheet.webp
```

不要重命名图集；三个 `pet.json` 的 `spritesheetPath` 都是 `spritesheet.webp`。GIF、预览页面、版本说明与校验清单不参与 Codex 加载。

## 3. 选择、更新与移除

复制完成后，在应用的宠物选择入口选择上表中的显示名。若列表没有更新，先重新打开应用，再核对文件层级。

更新同一款时，先备份对应宠物文件夹，再一起替换 `pet.json` 和 `spritesheet.webp`。移除某一款时，先在应用中切换到其他宠物，再移走该款文件夹。

## 预览动画

下载整个仓库并保持目录结构，用浏览器打开根目录 [preview.html](preview.html)。该页面用于切换三款宠物、9 组动作和 16 个看向方向。无需安装依赖；GitHub 页面中的 HTML 源码预览不会直接运行动画。

也可直接查看首页的 GIF，或两个服装版本各自的 `previews/`。通行证皮完整 ZIP 内另附旧版 `preview.html`，该页面只预览通行证皮。

## 通行证皮的 Work 图集

通行证皮额外提供 `mamuko-pass-v2/chatgpt/spritesheet.webp`。这是另一份图集，保留原有文件；Codex 安装使用 `mamuko-pass-v2/mamuko-pass/spritesheet.webp`。

Work 导入需要在你自己的账号中完成，流程见[通行证皮原有说明](mamuko-pass-v2/README.md#chatgpt-work-导入)。本次仓库整理未验证当前 Work 应用的导入入口，也未给原版和羁绊 v2 新增 Work 专用包。

## 常见问题

| 现象 | 检查方法 |
| --- | --- |
| 找不到宠物 | 确认应用支持自定义宠物，并检查 `pet.json` 是否直接位于 `.codex/pets/对应ID/`，没有多套一层文件夹。 |
| 图片为空或加载失败 | 确认 `pet.json` 与 `spritesheet.webp` 同层、图集文件名没有改变，ZIP 已完整解压。 |
| 动画切换与预览不同 | 预览页面手动播放动作；实际动作何时触发由应用控制。 |
| 更新后仍显示旧形象 | 检查是否复制到当前用户的目录，以及是否仍有旧 ID 的重复目录；备份后重新替换对应两文件并重开应用。 |
| 本地预览打不开图集 | 保持完整仓库目录结构，使用浏览器打开本地 `preview.html`，不要把 HTML 单独移动到别处。 |

## 文件校验

根目录 [release-manifest.json](release-manifest.json) 汇总三个下载包的摘要与规格；维护者可按 [MAINTAINING.md](MAINTAINING.md) 运行统一验证脚本。

通行证皮的 `package-manifest.json` 为逐文件清单；羁绊 v2 清单记录图集与 ZIP 的 SHA-256。两份清单保持原有结构。校验时相对路径以清单所在目录为起点。

在 Windows PowerShell 中可计算下载包摘要，例如：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\downloads\mamuko-pass-v2.zip
```

该命令应在仓库根目录运行。通行证皮 ZIP 的历史摘要另见 [SECURITY-CHECK.md](SECURITY-CHECK.md)；该文件只代表其中注明日期与范围的历史检查。

[返回仓库首页](README.md)

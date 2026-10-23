# 天川真梦梓 · 三款桌宠合集

收录天川真梦梓的**原版、通行证皮、羁绊 v2** 三款 Codex 自定义桌宠。三款使用不同的宠物 ID，可以同时安装。

| 原版 | 通行证皮 | 羁绊 v2 |
| --- | --- | --- |
| <img src="amakawa-mamuko/idle.gif" alt="原版待机预览" width="160"> | <img src="mamuko-pass-v2/previews/idle.gif" alt="通行证皮待机预览" width="160"> | <img src="mamuko-bond-v2/previews/idle.gif" alt="羁绊 v2 待机预览" width="160"> |
| **天川真梦梓** | **真梦梓 通行证皮** | **天川真梦梓 羁绊v2** |
| [下载安装 ZIP](downloads/amakawa-mamuko-v2.zip) | [下载完整 ZIP](downloads/mamuko-pass-v2.zip) | [下载安装 ZIP](downloads/amakawa-mamuko-bond-v2.zip) |
| [版本详情](amakawa-mamuko/README.md) | [版本详情与动画](mamuko-pass-v2/README.md) | [版本详情与动画](mamuko-bond-v2/README.md) |

## 快速安装

1. 下载所需版本的 ZIP，按[统一安装说明](INSTALL.md)解压。
2. 将该款的 `pet.json` 和 `spritesheet.webp` 放到当前用户 `.codex/pets/` 下对应的宠物文件夹中。两文件须同层。
3. 在支持自定义宠物的 Codex 版本中选择对应显示名；列表未更新时重新打开应用查看。

三个下载包的目录层级不同，详见[安装路径对照](INSTALL.md#2-放到正确位置)。预览 GIF、HTML 和清单无需复制到安装目录。

## 动画与预览

三款均使用透明 WebP 图集与 `spriteVersionNumber: 2` 配置：**1536 × 2288**，8 列 × 11 行，单格 192 × 208。

- 9 组标准动画：待机、向右移动、向左移动、挥手、跳跃、失落、等待输入、工作、审阅。
- 16 个看向方向：从正上方起，顺时针每隔 22.5° 一帧。
- 下载整个仓库后，用浏览器打开根目录 [preview.html](preview.html)，可以切换三款宠物、动作和看向方向。GitHub 文件页显示的是 HTML 源码；本地打开才能播放。
- 通行证皮另附 `chatgpt/spritesheet.webp`，使用方式见其[原有导入说明](mamuko-pass-v2/README.md#chatgpt-work-导入)。

预览用于检查素材；应用中的动作触发与状态切换由应用控制。

## 文件导航

```text
amakawa-mamuko/                  原版配置、图集与待机预览
mamuko-pass-v2/                  通行证皮安装文件、Work 图集与预览
mamuko-bond-v2/                  羁绊 v2 安装文件与预览
downloads/                      三款下载包
preview.html                    三款统一动画预览
INSTALL.md                      安装、更新与排错
MAINTAINING.md                  发布维护与校验方法
release-manifest.json            三款下载包的统一校验清单
```

各版本的旧路径与两个既有 ZIP 保持兼容；通行证皮和羁绊 v2 的原有清单见各自目录中的 `package-manifest.json`。原版新增下载包便于单独安装。

## 署名与记录

署名：**由宝ww / bilibili**。仓库当前未附 `LICENSE` 文件，未声明统一的开源许可证。

[SECURITY-CHECK.md](SECURITY-CHECK.md) 是 2026-10-04 通行证皮发布时的检查记录，检查范围与日期以该文件为准。本次整理后的包校验方法见 [MAINTAINING.md](MAINTAINING.md)。

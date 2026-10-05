# 天川真梦梓 羁绊v2

天川真梦梓羁绊服装的 Q 版 Codex 自定义宠物，按已确认的立绘制作，保留紫发蓝眸、黑色龙角、金色花饰、灰紫裙装与蓝色缎带。

[下载完整 ZIP](../downloads/amakawa-mamuko-bond-v2.zip) · [返回仓库首页](../README.md)

![已确认的 Q 版立绘](main-look-approved.png)

## 规格

- 显示名：**天川真梦梓 羁绊v2**
- 宠物 ID：`amakawa-mamuko-bond-v2`
- 配置：`spriteVersionNumber: 2`
- 透明 WebP：1536 × 2288，8 列 × 11 行，单格 192 × 208。
- 9 组标准动画、16 个顺时针看向方向，以及独立中立姿势。
- 精灵图格式、透明背景、帧数和方向已完成检查。

## 文件与安装

ZIP 内只有 `pet.json` 和 `spritesheet.webp`，两个文件须放在同一文件夹中。将它们解压到当前用户的 `.codex/pets/amakawa-mamuko-bond-v2/`，或直接复制本目录中的 `amakawa-mamuko-bond-v2` 文件夹到 `.codex/pets/`。

```text
.codex/pets/amakawa-mamuko-bond-v2/
  pet.json
  spritesheet.webp
```

## 动画预览

| 动作 | 预览 |
| --- | --- |
| 待机 | ![待机](previews/idle.gif) |
| 向右移动 | ![向右移动](previews/running-right.gif) |
| 向左移动 | ![向左移动](previews/running-left.gif) |
| 挥手 | ![挥手](previews/waving.gif) |
| 跳跃 | ![跳跃](previews/jumping.gif) |
| 失落 | ![失落](previews/failed.gif) |
| 等待输入 | ![等待输入](previews/waiting.gif) |
| 工作 | ![工作](previews/running.gif) |
| 审阅 | ![审阅](previews/review.gif) |

## 16 个看向方向

正上方为 000°，顺时针每隔 22.5° 一帧，覆盖正右、正下和正左。接近正下方的两个斜角水平偏转较细微，已结合连续方向检查。

![16 个看向方向](previews/look-directions.gif)

[查看逐方向对照](previews/look-directions.png) · [查看全部动作与方向](previews/contact-sheet.png)

文件校验信息见 [package-manifest.json](package-manifest.json)。
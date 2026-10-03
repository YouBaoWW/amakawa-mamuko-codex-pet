# 真梦梓 通行证皮 · v2 宠物包

紫色长发、黑金羽饰礼裙、蓝玫瑰与滑冰鞋；保留已审核的主形象、薄蓝色鞋跟和完整动画。

![真梦梓 通行证皮主形象](main-look-approved.png)

## 下载与版本

在仓库中下载 [完整 ZIP](../downloads/mamuko-pass-v2.zip)，解压后按下方说明选择对应版本。ZIP 内的 `mamuko-pass-v2` 文件夹包含本说明、图集和预览。

| 版本 | 文件 | 布局 |
| --- | --- | --- |
| Codex v2 | `mamuko-pass/pet.json` 和 `mamuko-pass/spritesheet.webp` | 8 列 × 11 行，1536 × 2288 像素，每帧 192 × 208 |
| ChatGPT Work v2 | `chatgpt/spritesheet.webp` | 同尺寸透明图集，按已审核的 Work v2 版本保留有效帧 |

两份图集均保留 9 组标准动画：待机、向右滑行、向左滑行、挥手、跳跃、失落、等待输入、工作、审阅。另有 16 个顺时针注视方向，从正上方起，每隔 22.5° 一帧。

## Codex 安装

1. 将本包中的 `mamuko-pass` 文件夹复制到当前用户的 `.codex/pets/` 下。
2. 保持 `pet.json` 与 `spritesheet.webp` 在同一层，不要重命名图集。
3. 在宠物选择入口选择“真梦梓 通行证皮”。如果列表尚未刷新，重新打开应用后再查看。

## ChatGPT Work 导入

将 `chatgpt/spritesheet.webp` 附给 ChatGPT Work 对话，使用 `work-pets:create-pet` 技能请求：“使用这份已完成的 v2 图集创建名为‘真梦梓 通行证皮’的宠物，保留现有图集、9 组动画与全部 16 个注视方向。”本包使用已验证的 Work Pets v2 导入流程。

导入过程需要在自己的账号中完成。安装完成后在宠物设置中选择它；Codex 的 `pet.json` 不用于这一导入流程。

## 查看动画

解压后打开 [preview.html](preview.html)，可切换动作、查看 16 个方向，并开启注视指针。该页面读取 Codex 图集，请保持它与 `mamuko-pass` 文件夹同层。

已交付的原始预览保存在 `previews/`：

- [完整状态 GIF](previews/all-states.gif) · [完整状态视频](previews/all-states.mp4)
- [待机 → 跳跃 → 待机](previews/idle-jump-idle-native.gif) · [16 个注视方向](previews/look-directions.gif)
- [逐帧总览](previews/contact-sheet.png) · [注视方向总览](previews/look-directions.png)
- [审核静帧拼图](previews/review-stills-montage.png)

各动作还提供独立 GIF，供下载后逐项查看。实际状态切换由应用控制。

## 文件校验与署名

`package-manifest.json` 记录本清单自身以外各发布文件的相对路径、字节数与 SHA-256。发布包中的图集、主形象和预览文件直接复制自已审核版本，未重新绘制或重编码。

署名：由宝ww/bilibili

# 通行证皮发布前安全检查

检查日期：2026-10-04。

本次使用 [api-key-leak-checker-leop](https://github.com/leo-cheung-itlger/api-key-leak-checker-leop) 的发布前检查脚本，以及 Gitleaks 8.30.1，检查新增宠物文件、下载 ZIP 和仓库已有提交历史。

## 检查结果

- skill 严格模式检查：退出码 0，无阻断项。
- Gitleaks 文件检查：退出码 0，未发现密钥；递归检查最多四层压缩文件。
- Gitleaks Git 历史检查：退出码 0，未发现密钥。
- GitHub Secret Scanning：已启用，检查时未处理告警数为 0。
- GitHub Push Protection：已启用。
- 新 ZIP 的 CRC、解压后文件一致性与 SHA-256 清单校验通过。
- 图集及预览与审核后的原始文件逐字节一致。

## 发布包整理

发布包仅包含宠物配置、图集、预览、说明和相对路径校验清单。未加入本地制作记录、机器绝对路径、ChatGPT 安装信息、私人 Library 文件标识、上传会话、缓存、渲染脚本或第三方运行库。

新增 `.gitignore`，排除本地环境配置、凭据、私钥、缓存与安装记录。

## 下载包校验

文件：`downloads/mamuko-pass-v2.zip`

字节数：`16392513`

SHA-256：`11edb3aa457518b6567fc4d6efd8c6e226fe54e0f30f5048961187a2cccde73d`

上述检查覆盖常见凭据模式与本次发布内容，不能保证识别所有秘密；后续新增文件应重新检查。

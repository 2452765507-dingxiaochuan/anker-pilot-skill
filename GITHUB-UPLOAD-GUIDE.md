# GitHub Public Repository 上传说明

## 推荐方式 A：GitHub Desktop（最简单）
1. 在 GitHub 新建一个 **Public** 仓库，例如 `anker-pilot-skill`。
2. 解压本上传包。
3. 用 GitHub Desktop：File → Add Local Repository / Create Repository from folder。
4. 选择解压后的 `anker-pilot-skill-v6-github` 文件夹。
5. Commit all → Publish / Push 到刚创建的 Public 仓库。

## 方式 B：终端
先在 GitHub 创建一个空的 Public 仓库，然后进入本文件夹：

```bash
git init
git add .
git commit -m "Anker Pilot V6 public exam pack"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>.git
git push -u origin main
```

## 方式 C：GitHub 网页上传
GitHub 网页上传对大量文件可能不如 Git/桌面客户端稳定。本包文件较多，优先使用 A 或 B。
如果只能网页上传：进入空仓库 → Add file → Upload files → 分批拖入解压后的目录内容，并保持目录结构。

## 上传成功后检查
仓库根目录至少应看到：
- `SKILL.md`
- `START-HERE.md`
- `OPEN_PROMPT_CONTROL_ROOM.html`
- `prompts/`
- `scenarios/`
- `knowledge/`
- `data/`
- `references/`
- `website/`
- `scripts/`
- `evals/`

仓库必须是 **Public**，否则公共考试电脑上的 Claude 在未登录 GitHub 时可能无法直接 clone / 读取。

# PROGRESS · 项目进度 〔本项目活记忆 · AI 维护〕

> **作用**：记录当前进度、决策、踩坑、下一步 TODO。按时间倒序。

---

## 2026-08-01 · 项目初始化

### 当前阶段

六步流程第 **①** 步：建仓 + 配 Secrets（仓库已存在，等待 Secrets 配置）

### 已完成

- [x] 仓库创建：`https://github.com/zmangmingyu/hello-flask-sz`
- [x] `standards/` 规范文件就位（00~06）
- [x] `standards/00-project-context.md` 已填写
- [x] `standards/01-requirements.md` 已填写（4 条用户故事 US-1 ~ US-4）

### 下一步 TODO

- [ ] 配置 GitHub Secrets（`SSH_PRIVATE_KEY` / `SSH_HOST` / `SSH_USER`）
- [ ] 从 `main` 开 `feature/1-hello-api` 分支
- [ ] 实现 `app.py` + `test_app.py` + `requirements.txt` + `Dockerfile` + CI/CD workflows
- [ ] 本地 CI 自检通过 → PR → 人工审核合并 → CD 部署

### ADR (Architecture Decision Records)

| 编号 | 决策 | 理由 |
|---|---|---|
| ADR-1 | 选择 Flask 而非 FastAPI | 教学项目，Flask 更轻量、入门成本更低 |
| ADR-2 | 端口 8003，容器内端口固定 | 配合标准 CD 部署脚本的端口回落机制 |

### GOTCHAS (踩坑记录)

无（项目刚开始）

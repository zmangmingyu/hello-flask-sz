# PROGRESS · hello-flask-sz 〔本项目活记忆 · 状态机〕

> **作用**:这是项目的"存档点"。任意 AI、任意重启会话,读它即可知道当前做到哪、下一步做什么、踩过什么坑。
> **更新时机**:每完成一个有意义步骤、每次会话结束前。
> **格式要求**:时间倒序,最新在上;短、准、可接力。

---

## 当前状态 (最后更新: 2026-06-06 · by AI)

- **阶段**: `已上线`
- **上一步完成**: CI/CD 全流程跑通,部署成功
- **下一步 (TODO 第一条)**: 功能已完成,可添加新需求
- **阻塞项**: 无

---

## 待办清单 (TODO,按优先级)

- [x] 用户确认 `00-project-context.md` 内容无误
- [x] 用户确认 `01-requirements.md` 用户故事和验收标准
- [x] 从 `main` 开第一条 feature 分支: `feature/1-init-project`
- [x] 创建基础文件: `app.py`, `test_app.py`, `requirements.txt`, `requirements-dev.txt`, `Dockerfile`
- [x] 实现欢迎接口 (`GET /`)
- [x] 实现健康检查接口 (`GET /health`)
- [x] 编写单元测试(覆盖率 >= 80%)
- [x] 本地自检: `ruff format --check .` + `ruff check .` + `pytest`
- [x] 创建 CI workflow (`.github/workflows/ci.yml`)
- [x] 创建 CD workflow (`.github/workflows/cd.yml`)
- [x] 创建 GitHub 仓库: https://github.com/DaTingLi/hello-flask-sz
- [x] 推送代码到 main
- [x] CI 验证: 格式/lint/测试/构建 全绿
- [x] CD 验证: 部署到端口 8003,健康检查通过

---

## 关键决策记录 (ADR)

| 日期 | 决策 | 理由 |
|---|---|---|
| 2026-06-06 | HTTPS 失败后切换 SSH | GitHub 443 端口连接超时,SSH 协议成功 |
| 2026-06-06 | 直接推送 main 跳过 PR | 新仓库 main 为空,无法创建 PR,直接初始化 |

---

## 已知坑 (GOTCHAS)

- **HTTPS 连接 GitHub 443 超时**: 现象:`Failed to connect to github.com port 443`;根因:网络限制;解决:`git remote set-url origin` 切换 SSH;验证:`git push` 成功
- **新仓库 main 为空无法 PR**: 现象:`No commits between main and feature`;根因:main 分支不存在;解决:直接推送 main 或先创建占位提交;验证:仓库有 main 分支

---

## 里程碑 (DONE)

- [x] US-1 初始化项目工程化与 CI/CD - CI/CD 全流程跑通
- [x] US-2 实现欢迎接口 - `GET /` 返回欢迎 JSON
- [x] US-3 实现健康检查接口 - `GET /health` 返回 `{"status":"ok"}`
- [x] US-4 容器化部署 - Docker 构建与部署成功

**部署信息**:
- 仓库: https://github.com/DaTingLi/hello-flask-sz
- 端口: 8003
- 健康检查: `/health`
- 覆盖率: 97.67%

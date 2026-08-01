# PROGRESS · hello-flask-sz 〔本项目活记忆 · 状态机〕

> **作用**:这是项目的"存档点"。任意 AI、任意重启会话,读它即可知道当前做到哪、下一步做什么、踩过什么坑。
> **更新时机**:每完成一个有意义步骤、每次会话结束前。
> **格式要求**:时间倒序,最新在上;短、准、可接力。

---

## 当前状态 (最后更新: 2026-08-01 · by AI)

- **阶段**: `项目初始化` (对应 06 六步流程 第①步)
- **上一步完成**: 建仓 `https://github.com/zmangmingyu/hello-flask-sz` + 最小引导提交已推送 main
- **下一步 (TODO 第一条)**: ⚠️ 人类配置 GitHub Secrets (`SSH_PRIVATE_KEY` / `SSH_HOST` / `SSH_USER`)
- **阻塞项**: Secrets 未配置,无法进入 CD

---

## 待办清单 (TODO,按优先级)

- [ ] ⚠️ **人类配置 Secrets**: `Settings → Secrets and variables → Actions → New repository secret` 添加 `SSH_PRIVATE_KEY` / `SSH_HOST` / `SSH_USER`
- [ ] 从 `main` 开第一条 feature 分支: `feature/1-init-project`
- [ ] 创建基础文件: `app.py`, `test_app.py`, `requirements.txt`, `requirements-dev.txt`, `Dockerfile`
- [ ] 实现欢迎接口 (`GET /`)
- [ ] 实现健康检查接口 (`GET /health`)
- [ ] 编写单元测试(覆盖率 >= 80%)
- [ ] 本地自检: `ruff format --check .` + `ruff check .` + `pytest`
- [ ] 创建 CI workflow (`.github/workflows/ci.yml`)
- [ ] 创建 CD workflow (`.github/workflows/cd.yml`)
- [ ] 推送代码 → 提 PR → CI 验证
- [ ] 合并 main → CD 自动部署 → 端口 8003 健康检查通过

---

## 关键决策记录 (ADR)

| 日期 | 决策 | 理由 |
|---|---|---|
| 2026-08-01 | 使用 `gh` CLI 建仓,HTTPS 协议推送 | gh 已登录 zmangmingyu,Token 权限完整(repo/workflow) |

---

## 已知坑 (GOTCHAS)

_暂无_

---

## 里程碑 (TODO)

- [ ] US-1 初始化项目工程化与 CI/CD
- [ ] US-2 实现欢迎接口
- [ ] US-3 实现健康检查接口
- [ ] US-4 容器化部署

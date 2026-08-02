# PROGRESS · 项目进度 〔本项目活记忆 · AI 维护〕

> **作用**：记录当前进度、决策、踩坑、下一步 TODO。按时间倒序。

---

## 2026-08-02 · 本地开发 + CI 自检通过（本次会话）

### 当前阶段

六步流程第 **⑤** 步：触发 PR（待 push + gh pr create）

### 已完成

- [x] `standards/00-project-context.md` — 技术栈: Python 3.11 / Flask / pytest / ruff / Docker, 端口 8003
- [x] `standards/01-requirements.md` — 4 条用户故事 US-1~US-4, 每条带验收标准
- [x] Step ②: 从 main 切出 `feature/1-hello-api`, rebase 到最新 main
- [x] Step ③: 代码文件验证通过:
  - `app.py` — Flask 入口, `GET /` + `GET /health`, 端口 8003
  - `test_app.py` — 7 条测试(含边界 404)
  - `requirements.txt` / `requirements-dev.txt` — 生产与开发依赖拆分
  - `Dockerfile` — Python 3.11-slim, 支持 `PIP_INDEX_URL` 镜像源参数
  - `.github/workflows/ci.yml` — PR 触发 ruff + pytest + cov + docker build
  - `.github/workflows/cd.yml` — push main 触发 SSH 部署 + Docker 镜像加速 + 端口回退 + 健康检查
  - `.gitignore` / `README.md`
- [x] Step ④: 本地 CI 自检**全绿**:
  - `ruff format --check .` — 15 files already formatted ✅
  - `ruff check .` — All checks passed ✅
  - `pytest --cov=. --cov-fail-under=80` — 7 passed, 98% 覆盖率 ✅

### 下一步 TODO

- [ ] Step ⑤: push + `gh pr create`, 等 CI 绿灯
- [ ] Step ⑥: ✋ 人工 Review + Merge → CD 自动部署 → 验证 `/health`

---

## 2026-08-01 · 项目初始化

### 当前阶段（当时）

六步流程第 **①** 步：建仓 + 配 Secrets（仓库已存在）

### 已完成（当时）

- [x] 仓库创建：`https://github.com/zmangmingyu/hello-flask-sz`
- [x] `standards/` 规范文件就位（00~06）
- [x] `standards/00-project-context.md` 已填写
- [x] `standards/01-requirements.md` 已填写（4 条用户故事 US-1 ~ US-4）

### ADR (Architecture Decision Records)

| 编号 | 决策 | 理由 |
|---|---|---|
| ADR-1 | 选择 Flask 而非 FastAPI | 教学项目，Flask 更轻量、入门成本更低 |
| ADR-2 | 端口 8003，容器内端口固定 | 配合标准 CD 部署脚本的端口回落机制 |

### GOTCHAS (踩坑记录)

| 编号 | 现象 | 根因 | 修复 |
|---|---|---|---|
| GOTCHA-1 | 本地只有 Python 3.14, 无 3.11 | 开发机未装 3.11 | 本地用 3.14 开发(兼容), CI 按 workflow 指定 3.11 |
| GOTCHA-2 | Python 3.14 + 中文路径导致 pytest 输出乱码 | 路径含中文 `standards训练` | Windows 控制台编码问题, 不影响 CI(Linux runner) |

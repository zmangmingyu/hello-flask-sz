# PROGRESS · 项目进度 〔本项目活记忆 · AI 维护〕

> **作用**：记录当前进度、决策、踩坑、下一步 TODO。按时间倒序。

---

## 2026-08-02 · 全链路跑通 ✅（本次会话）

### 当前阶段

六步流程第 **⑥** 步 — **已完成!** 全链路 `①→②→③→④→⑤→⑥` 跑通。

### 部署结果

| 项目 | 值 |
|---|---|
| ⚠️ **实际主机端口** | **8008** |
| 容器内端口 | 8003 |
| 端口回落原因 | 8003 被占用,CD 脚本自动在 8003-8020 区间回退 |
| 健康检查 | `http://172.16.0.7:8008/health` ✅ |
| 服务地址 | `http://<SSH_HOST>:8008` |

### 已完成

- [x] Step ①: 仓库与 Secrets 已配置
- [x] Step ②: `feature/1-hello-api` → rebase main → push
- [x] Step ③: 代码文件验证通过(app.py / test_app.py / CI/CD / Dockerfile / README)
- [x] Step ④: 本地 CI 自检全绿(ruff ✅ ruff check ✅ pytest 7/7 98% ✅)
- [x] Step ⑤: PR #4 创建 + CI 绿灯 ✅
- [x] Step ⑥: 人工 Merge → CD 自动部署 → `/health` 通过 → **部署端口 8008** ✅

### 下一步 TODO

- 无(US-1~US-4 全部完成)

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

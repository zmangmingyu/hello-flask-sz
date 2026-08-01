# 01 · 需求 / 活 PRD 〔本项目活记忆 · AI 维护〕

> **作用**:这是本项目唯一的需求文档。所有新功能、缺陷、技术债都追加到这里,不要另起多个 PRD 文件。
> **更新时机**:每次有新需求、需求变更、验收标准变化时更新。

---

## 1. 需求来源

| 类型 | 来源 | 进入方式 |
|---|---|---|
| 功能需求 Feature | 课程教学需求 | 写成用户故事 |
| 缺陷 Bug | 测试 / CI/CD 失败 | 写复现步骤和期望结果 |
| 技术债 Tech Debt | Review / CI/CD 故障 | 写影响和修复目标 |

---

## 2. Issue 生命周期

| 阶段 | 状态 | 动作 |
|---|---|---|
| 提出 | Open | 写清场景、目标、验收标准 |
| 排期 | Backlog / Todo | 决定优先级和负责人 |
| 开发 | In Progress | 从 main 开 feature 分支 |
| 评审 | In Review | 提 PR,等待 CI 和 Review |
| 合并 | Done | PR 合并 main,自动关闭 Issue |
| 验收 | Verified | 按验收标准确认 |

**追踪规则**:分支名带 Issue 号,PR 描述写 `closes #<编号>`。

---

## 3. 用户故事模板

```text
### US-<编号> <一句话标题> · 状态: Backlog
作为 <角色>,
我想要 <能力>,
以便 <价值>。

验收标准:
- AC1: Given <前提>,When <动作>,Then <可验证结果>。
- AC2: <补充标准>

技术备注:
- <可选:约束、边界、风险>
```

---

## 4. 需求清单

### US-1 初始化项目工程化与 CI/CD · 状态: Backlog

作为 **项目开发者**,
我想要 项目具备基础工程结构、测试、CI 与 CD,
以便 后续每次开发都能自动检查并自动部署。

验收标准:
- AC1: 从 `main` 开 feature 分支完成初始化,不直接 push main。
- AC2: PR 触发 CI,至少包含格式检查、静态检查、单元测试、构建检查。
- AC3: CI 全绿后合并 main。
- AC4: 合并 main 自动触发 CD,部署后健康检查通过。
- AC5: 完成后更新 `standards/PROGRESS.md`。

### US-2 实现欢迎接口 · 状态: Backlog

作为 **网站访客**,
我想要 访问根路径时获得欢迎响应,
以便 确认服务正常运行。

验收标准:
- AC1: Given 服务已启动,When 访问 `GET /`,Then 返回状态码 200。
- AC2: Given 服务已启动,When 访问 `GET /`,Then 返回 JSON 包含欢迎消息(如 `{"message": "Welcome to hello-flask-sz"}`)。
- AC3: Given 服务已启动,When 用浏览器访问 `http://localhost:8003`,Then 能看到 JSON 响应。

技术备注:
- 使用 Flask 路由 `@app.route('/')` 实现。
- 返回 `jsonify` 确保响应头为 `application/json`。

### US-3 实现健康检查接口 · 状态: Backlog

作为 **运维 / 部署系统**,
我想要 通过 `/health` 接口检查服务状态,
以便 在部署后验证服务健康。

验收标准:
- AC1: Given 服务已启动,When 访问 `GET /health`,Then 返回状态码 200。
- AC2: Given 服务已启动,When 访问 `GET /health`,Then 返回 JSON `{"status": "ok"}`。
- AC3: Given CD 部署完成,When 执行 `curl http://localhost:8003/health`,Then 响应时间 < 2 秒。

技术备注:
- 这是 CD 健康检查的标准接口,不可改名或删除。
- 不依赖数据库或外部服务,确保始终可达。

### US-4 容器化部署 · 状态: Backlog

作为 **运维工程师**,
我想要 服务以 Docker 容器运行,
以便 统一部署环境并支持 CI/CD。

验收标准:
- AC1: Given Dockerfile 已就绪,When 执行 `docker build -t hello-flask-sz:latest .`,Then 构建成功无错误。
- AC2: Given 镜像已构建,When 执行 `docker run -d -p 8003:8003 --name hello-flask-sz hello-flask-sz:latest`,Then 容器正常启动。
- AC3: Given 容器已运行,When 访问 `http://localhost:8003/health`,Then 返回 `{"status": "ok"}`。

技术备注:
- Dockerfile 使用官方 Python 3.11 基础镜像。
- 支持镜像源参数,便于国内服务器使用清华源。
- 容器内端口固定 8003。

---

## 5. 非功能需求

- **安全**:密钥只进 Secrets,不进 Git。
- **可维护**:一需求一小 PR,避免大爆炸式提交。
- **可测试**:核心逻辑必须有单元测试,覆盖率 >= 80%。
- **可部署**:部署后 `/health` 必须返回 200。
- **代码质量**:通过 ruff 格式检查和静态检查。

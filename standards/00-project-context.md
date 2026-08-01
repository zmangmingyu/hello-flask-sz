# 00 · 项目上下文 〔本项目活记忆 · AI 维护〕

> **作用**:这是项目的"身份档案"。AI 接管项目时先读这里,了解项目目标、技术栈、目录、部署取值。
> **更新时机**:架构、技术栈、目录结构、端口、部署目录、重要约束变化时更新。
> **填写方式**:把 `<...>` 替换成真实内容;用不到的行删掉。

---

## 1. 项目是什么

- **项目名称**: `hello-flask-sz`
- **一句话目标**: 一个最小 Flask Web 服务示例,跑通 CI/CD 全流程
- **使用者/受益者**: 学习 DevOps 和 Flask 开发的学生
- **核心功能**:
  - GET `/` 返回欢迎 JSON
  - GET `/health` 返回 `{"status":"ok"}` 供健康检查
- **输入/数据**: 无

## 2. 技术栈

| 层 | 选型 | 理由 |
|---|---|---|
| 语言/运行时 | Python 3.11 | 教学常用版本,稳定 |
| Web/API 框架 | Flask | 轻量、适合教学 |
| 测试 | pytest | Python 标准测试框架 |
| 格式/静态检查 | ruff | 快速、现代化 |
| 打包/运行 | Docker | 标准容器化部署 |
| CI/CD | GitHub Actions | 通用、可视化、适合教学 |

## 3. 目录地图

```text
hello-flask-sz/
├── standards/                 # AI 项目记忆与通用规范
├── app.py                     # Flask 应用入口
├── test_app.py                # 测试文件
├── requirements.txt           # 生产依赖
├── requirements-dev.txt       # 开发依赖
├── Dockerfile                 # 容器构建
├── .github/workflows/
│   ├── ci.yml
│   └── cd.yml
└── README.md
```

> 新增目录前先更新本节,避免项目越做越散。

## 4. 质量门槛

| 类型 | 本项目标准 |
|---|---|
| 格式检查 | `ruff format --check .` |
| 静态检查 | `ruff check .` |
| 单元测试 | `pytest` |
| 覆盖率 | >=80% |
| 构建 | `docker build` 成功 |
| 业务/模型指标 | 无 |

## 5. 不变约束

- 密钥、密码、私钥、Token **绝不写进代码或文档**,只进 GitHub Secrets / 环境变量。
- `main` 分支受保护,日常开发必须走 feature 分支 + PR。
- CI 红灯不合并。

## 6. 部署/CI 占位符取值

> `guides/` 和 workflow 里的通用占位符,在本项目里的真实值只写这里。

| 占位符 | 本项目取值 | 说明 |
|---|---|---|
| `<APP>` | `hello-flask-sz` | 应用名/镜像名/容器名 |
| `<DEPLOY_DIR>` | `/opt/hello-flask-sz` | 服务器部署目录 |
| `<PORT>` | `8003` | 服务端口 |
| `<PORT_MAX>` | `8020` | 端口回退上限 |
| `<PYVER>` | `3.11` | Python 版本 |
| `<HEALTHCHECK>` | `/health` | 健康检查地址 |
| `<SSH_USER>` | `root` | 部署用户(示例) |
| `<SSH_HOST>` | `<服务器IP>` | 服务器地址(由学生配置) |

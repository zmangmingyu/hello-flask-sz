# hello-flask-sz

最小 Flask Web 服务示例，跑通 CI/CD 全流程。

## 快速开始

```bash
pip install -r requirements.txt
python app.py
```

访问 http://localhost:8003

## 接口

| 路径 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 返回欢迎 JSON |
| `/health` | GET | 返回 `{"status":"ok"}` 健康检查 |

## 技术栈

Python 3.11 · Flask · pytest · ruff · Docker

## 部署

| 项目 | 值 |
|---|---|
| 部署方式 | Docker 容器, CD 自动部署 |
| 容器内端口 | 8003 |
| ⚠️ **实际主机端口** | **8008**（8003 被占用,CD 端口回退机制自动分配） |
| 健康检查 | `http://<服务器IP>:8008/health` |

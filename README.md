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

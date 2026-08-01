"""hello-flask-sz · 最小 Flask Web 服务."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """欢迎接口：返回 JSON 欢迎消息。"""
    return jsonify({"message": "Welcome to hello-flask-sz"})


@app.route("/health")
def health():
    """健康检查接口：返回服务状态。"""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)

"""hello-flask-sz 测试."""

import pytest

from app import app


@pytest.fixture
def client():
    """Flask 测试客户端 fixture。"""
    app.config["TESTING"] = True
    return app.test_client()


class TestIndex:
    """GET / 欢迎接口测试。"""

    def test_index_returns_200(self, client):
        """AC1: 访问 GET / 返回状态码 200。"""
        resp = client.get("/")
        assert resp.status_code == 200

    def test_index_returns_json(self, client):
        """AC2: 返回 JSON 且 content-type 正确。"""
        resp = client.get("/")
        assert resp.content_type == "application/json"

    def test_index_returns_welcome_message(self, client):
        """AC2: 返回 JSON 包含欢迎消息。"""
        resp = client.get("/")
        data = resp.get_json()
        assert "message" in data
        assert "hello-flask-sz" in data["message"].lower()


class TestHealth:
    """GET /health 健康检查测试。"""

    def test_health_returns_200(self, client):
        """AC1: 访问 /health 返回状态码 200。"""
        resp = client.get("/health")
        assert resp.status_code == 200

    def test_health_returns_status_ok(self, client):
        """AC2: 返回 JSON {"status": "ok"}。"""
        resp = client.get("/health")
        data = resp.get_json()
        assert data == {"status": "ok"}

    def test_health_content_type_is_json(self, client):
        """响应 content-type 为 application/json。"""
        resp = client.get("/health")
        assert resp.content_type == "application/json"


class TestEdgeCases:
    """边界与异常测试。"""

    def test_nonexistent_route_returns_404(self, client):
        """访问不存在的路由应返回 404。"""
        resp = client.get("/nonexistent")
        assert resp.status_code == 404

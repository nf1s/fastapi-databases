# -*- coding: utf-8 -*-
""" FastAPI databases tests module
"""
from main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_get_request():
    response = client.get("/user/get")
    assert response.status_code == 200
    assert response.json() == {
        "firstName": "John",
        "lastName": "Doe",
        "age": 30,
    }

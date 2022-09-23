import os
from unittest import mock
from flask import session
import pytest
from pytest_mock import mocker

from ticket_website import create_app


@pytest.fixture
@mock.patch.dict(os.environ, {"DATABASE_URL": "test_url"}, clear=True)
def app(mocker):
    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)

    app = create_app()
    return app


def test_auth_signup_page_accessable(client):
    response = client.get("/signup")
    assert response.status_code == 200


def test_auth_login_page_accessable(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_logout_redirects_to_login_page(client):
    response = client.get("/logout", follow_redirects=True)
    assert len(response.history) == 1    
    assert response.request.path == "/login"

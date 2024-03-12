import os
import pytest
from app import create_app, db
from tests import DevelopementConfig

env_name = os.getenv("FLASK_ENV", "development")
@pytest.fixture()
def app():
    
    app = create_app(env_name)

    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_get(client):
    response = client.get("/")
    assert response.status_code == 200

def test_post(client):
    response = client.post("/", json={'name': 'Usuario'})
    assert response.status_code == 200

def test_delete(client):
    response = client.delete("/1")
    assert response.status_code == 200

# https://werkzeug.palletsprojects.com/en/2.3.x/test/#werkzeug.test.EnvironBuilder
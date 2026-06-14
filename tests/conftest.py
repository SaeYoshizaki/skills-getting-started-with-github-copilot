import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities = app_module.get_default_activities()
    yield
    app_module.activities = app_module.get_default_activities()


@pytest.fixture
def client():
    return TestClient(app_module.app)

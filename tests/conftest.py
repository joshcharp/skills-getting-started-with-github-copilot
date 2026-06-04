import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Create a FastAPI test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activity participants after each test."""
    original_state = copy.deepcopy(activities)

    yield

    activities.clear()
    activities.update(copy.deepcopy(original_state))

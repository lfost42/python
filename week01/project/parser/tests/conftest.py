"""
Fixtures to initialize tests.
"""
import pytest
from app import app

@pytest.fixture(scope='module')
def test_client():
    """A fixture to initialize tests.

    Returns:
        Route: To the test client.
    """
    return app.test_client()

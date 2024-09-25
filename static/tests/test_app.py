import pytest
from app import app, db, Product  # Ensure 'app.py' is in the same directory or adjust the import path

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
def test_index(client):
    response = client.get('/')
    assert b'Welcome to the Simple Store!' in response.data
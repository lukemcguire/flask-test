import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add/2/3')
    assert response.status_code == 200
    assert response.data == b'5'

    response = client.get('/add/-1/1')
    assert response.status_code == 200
    assert response.data == b'0'

def test_fibonacci(client):
    response = client.get('/fibonacci/1')
    assert response.status_code == 200
    assert response.data == b'0'

    response = client.get('/fibonacci/2')
    assert response.status_code == 200
    assert response.data == b'1'

    response = client.get('/fibonacci/5')
    assert response.status_code == 200
    assert response.data == b'3'

    response = client.get('/fibonacci/10')
    assert response.status_code == 200
    assert response.data == b'55'

    response = client.get('/fibonacci/0')
    assert response.status_code == 200
    assert response.data == b'Invalid input'

    response = client.get('/fibonacci/-1')
    assert response.status_code == 200
    assert response.data == b'Invalid input'

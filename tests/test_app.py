import pytest

from app import app, fibonacci


@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Tests the hello endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "hello world"


def test_add(client):
    """Tests the add endpoint with various inputs."""
    # Test positive numbers
    response = client.get("/add/1/2")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "3"

    # Test zero
    response = client.get("/add/0/0")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "0"

    # Test negative numbers
    response = client.get("/add/%2D1/1")  # Using URL-encoded minus sign
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "0"

    # Additional negative number test cases
    response = client.get("/add/%2D5/3")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "-2"


def test_fibonacci_function():
    """Tests the fibonacci function directly."""
    # Test invalid input
    assert fibonacci(0) == "Invalid input"
    assert fibonacci(-1) == "Invalid input"

    # Test base cases
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1

    # Test other valid inputs
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8


def test_fibonacci_endpoint(client):
    """Tests the fibonacci endpoint with various inputs."""
    # Test valid inputs
    response = client.get("/fibonacci/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "0"

    response = client.get("/fibonacci/7")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "8"

    # Test invalid input type (will be caught by Flask's routing)
    response = client.get("/fibonacci/invalid")
    assert response.status_code == 404

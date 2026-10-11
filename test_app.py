import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200

def test_high_performance_prediction(client):
    payload = {
        "attendance": 90,
        "internal_marks": 85,
        "assignment_marks": 88,
        "previous_score": 80
    }
    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["prediction"] == "PASS"
    assert data["prediction_code"] == 1

def test_low_performance_prediction(client):
    payload = {
        "attendance": 55,
        "internal_marks": 30,
        "assignment_marks": 40,
        "previous_score": 35
    }
    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["prediction"] == "FAIL"
    assert data["prediction_code"] == 0

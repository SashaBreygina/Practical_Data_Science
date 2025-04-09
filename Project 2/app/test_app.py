import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    res = requests.get(BASE_URL + "/")
    assert res.status_code == 200

def test_get_personas():
    res = requests.get(BASE_URL + "/personas")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_feedback():
    res = requests.get(BASE_URL + "/feedback/0")
    assert res.status_code == 200
    assert "feedback" in res.json()

if __name__ == "__main__":
    test_root()
    test_get_personas()
    test_feedback()
    print("All tests passed!")

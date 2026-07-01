import requests
import pytest_check as check
import pytest

headers = {
    "x-api-key" : "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
}

@pytest.mark.api
@pytest.mark.smoke
def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    assert response.status_code == 200

@pytest.mark.api
def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing password"

@pytest.mark.api
def test_login_sin_email():
    body = {
        "password": "cityslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing email or username"

@pytest.mark.api
def test_create_user():
    body = {
        "name": "Jose",
        "email": "jose.montezuma@bue.edu.ar",
        "password": "12345*"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers,json=body)

    data = response.json()

    assert response.status_code == 201
    #check.equal(response.status_code,201)
    
    #assert body["email"].count("@") == 1
    check.equal(body["email"].count("@"),1)
    #assert "*" in body["password"]
    check.is_in("*",body["password"])

    #assert data["name"] == body["name"]
    check.equal(data["name"],body["name"])
    #assert data["email"] == body["email"]
    check.equal(data["email"],body["email"])

    #assert response.elapsed.total_seconds() < 1
    check.less(response.elapsed.total_seconds(),1)

@pytest.mark.api
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2",headers=headers)

    assert response.status_code == 204

@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/2",headers=headers)

    assert response.status_code == 200
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion tardo mas de lo esperado"
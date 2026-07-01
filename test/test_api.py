import requests
import pytest_check as check
import pytest

from utils.logger import logger

headers = {
    "x-api-key" : "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
}

@pytest.mark.api
@pytest.mark.smoke
def test_login_valido():
    logger.info("Iniciando test_login_valido: POST /api/login con credenciales validas")
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    logger.info(f"Status code recibido: {response.status_code}")
    assert response.status_code == 200

@pytest.mark.api
def test_login_sin_password():
    logger.info("Iniciando test_login_sin_password: POST /api/login sin campo password")
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    logger.info(f"Status code: {response.status_code}, error recibido: {body.get('error')}")
    assert response.status_code == 400
    assert body["error"] == "Missing password"

@pytest.mark.api
def test_login_sin_email():
    logger.info("Iniciando test_login_sin_email: POST /api/login sin campo email")
    body = {
        "password": "cityslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    logger.info(f"Status code: {response.status_code}, error recibido: {body.get('error')}")
    assert response.status_code == 400
    assert body["error"] == "Missing email or username"

@pytest.mark.api
def test_create_user():
    logger.info("Iniciando test_create_user: POST /api/users")
    body = {
        "name": "Jose",
        "email": "jose.montezuma@bue.edu.ar",
        "password": "12345*"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers,json=body)

    data = response.json()
    logger.info(f"Status code: {response.status_code}, usuario creado: {data.get('name')}")

    assert response.status_code == 201

    logger.info("Validando estructura y contenido de la respuesta")
    check.equal(body["email"].count("@"),1)
    check.is_in("*",body["password"])
    check.equal(data["name"],body["name"])
    check.equal(data["email"],body["email"])
    check.less(response.elapsed.total_seconds(),1)

@pytest.mark.api
def test_delete_user():
    logger.info("Iniciando test_delete_user: DELETE /api/users/2")
    response = requests.delete("https://reqres.in/api/users/2",headers=headers)

    logger.info(f"Status code recibido: {response.status_code}")
    assert response.status_code == 204

@pytest.mark.api
def test_get_user():
    logger.info("Iniciando test_get_user: GET /api/users/2")
    response = requests.get("https://reqres.in/api/users/2",headers=headers)

    logger.info(f"Status code: {response.status_code}, tiempo de respuesta: {response.elapsed.total_seconds()}s")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion tardo mas de lo esperado"

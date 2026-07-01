from page.login_page import LoginPage
from utils.data_reader import read_users_csv
from utils.logger import logger
import pytest

@pytest.mark.parametrize("user",read_users_csv())
def test_login(driver,user):
    logger.info(f"Iniciando test_login parametrizado con usuario: {user['username']}")
    login_page = LoginPage(driver)

    logger.info("Realizando login con las credenciales del CSV")
    login_page.login(user["username"],user["password"])

    if user["valid"] == "true":
        logger.info("Caso esperado: login valido, verificando redireccion al inventario")
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        logger.info("Caso esperado: login invalido, verificando mensaje de error")
        error = login_page.get_error_message()
        assert "Epic sadface" in error

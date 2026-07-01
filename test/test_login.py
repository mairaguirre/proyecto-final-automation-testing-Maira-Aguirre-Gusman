from page.login_page import LoginPage
from utils.logger import logger
import pytest

@pytest.mark.smoke
def test_login_ok(driver):
    logger.info("Inicializando el driver para test_login_ok")
    login_page = LoginPage(driver)
    
    logger.info("Ingresando los datos de entrada para la prueba")
    login_page.login("standard_user","secret_sauce")

    logger.info("Iniciando sesion...")

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","123456")

    error = login_page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error


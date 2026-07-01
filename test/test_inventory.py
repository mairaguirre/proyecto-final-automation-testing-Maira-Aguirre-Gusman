from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.login_page import LoginPage
from utils.logger import logger

def test_inventory_title(driver_logged):
    logger.info("Iniciando test_inventory_title")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Obteniendo el titulo de la pagina de inventario")
    titulo = inventory_page.obtener_titulo()

    logger.info(f"Validando que el titulo sea 'Swag Labs' (obtenido: '{titulo}')")
    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"

@pytest.mark.smoke
def test_productos_visibles(driver_logged):
    logger.info("Iniciando test_productos_visibles")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Obteniendo la lista de productos del inventario")
    productos = inventory_page.obtener_productos()

    logger.info(f"Se encontraron {len(productos)} productos, validando que sea mayor a 0")
    assert len(productos) > 0

def test_ui_elements(driver_logged):
    logger.info("Iniciando test_ui_elements")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Verificando visibilidad del menu")
    assert inventory_page.menu_visible(), "El menu no está presente en la pagina"

    logger.info("Verificando visibilidad del filtro de orden")
    assert inventory_page.filtro_visible(), "El filtro no está presente en la pagina"

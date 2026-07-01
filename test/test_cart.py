from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from utils.logger import logger

@pytest.mark.smoke
def test_cart(driver_logged):
    logger.info("Iniciando test_cart")
    driver = driver_logged

    logger.info("Agregando el primer producto disponible al carrito")
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    logger.info("Verificando que el contador del carrito sea 1")
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"

    logger.info("Obteniendo el nombre del producto agregado")
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    logger.info("Ingresando al carrito")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    logger.info("Obteniendo el nombre del producto dentro del carrito")
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    logger.info(f"Comparando producto agregado ('{product_name}') vs producto en carrito ('{cart_item}')")
    assert cart_item == product_name, "El producto agregado no coincide"

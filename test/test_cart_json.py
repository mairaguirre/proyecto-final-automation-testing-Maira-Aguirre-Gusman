from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import logger

def test_cart_json(driver_logged):
    logger.info("Iniciando test_cart_json")
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)

    logger.info("Leyendo productos esperados desde data/products.json")
    productos = read_products_json()
    logger.info(f"Se cargaron {len(productos)} productos desde el JSON")

    for producto in productos:
        logger.info(f"Agregando producto al carrito: {producto['nombre']}")
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

    logger.info("Ingresando al carrito")
    inventory_page.ir_al_carrito()

    logger.info("Obteniendo productos actualmente en el carrito")
    productos_carrito = cart_page.obtener_productos_carrito()

    for producto_json in productos:
        logger.info(f"Verificando que '{producto_json['nombre']}' esté en el carrito con el precio correcto")
        encontrado = False
        for producto_carrito in productos_carrito:
            if ( (producto_carrito["nombre"] == producto_json["nombre"]) and (producto_carrito["precio"] == producto_json["precio"])):
                encontrado = True
                break

        assert encontrado, f"Producto incorrecto o faltante: {producto_json["nombre"]}"

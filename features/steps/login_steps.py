from page.login_page import LoginPage
from behave import given,when,then

@given("que el usuario está en la pagina de Login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when("ingresa el usuario '{usuario}' y la contreseña '{password}'")
def step_ingresar_credenciales(context,usuario,password):
    if usuario == "VACIO":
        usuario = ""
    
    if password == "VACIO":
        password = ""

    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_password(password)

@when("hace clic en el boton Login")
def step_click_login(context):
    context.login_page.click_login()

@then("deberia ingresar al inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url, "No se redirigió al inventario"

@then("deberia ver el mensaje de error '{mensaje}'")
def step_validar_mensaje_error(context,mensaje):
    error = context.login_page.get_error_message()
    assert mensaje in error, f"Se esperaba '{mensaje}, pero se obtuvo {error}'"
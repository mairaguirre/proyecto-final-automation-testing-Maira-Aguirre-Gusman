@login
Feature: Inicio de sesion
    Background:
        Given que el usuario está en la pagina de Login

    @postivo
    Scenario: Login exitoso
        When ingresa el usuario 'standard_user' y la contreseña 'secret_sauce'
        And hace clic en el boton Login
        Then deberia ingresar al inventario

    @negativo
    Scenario: Login invalido con contreseña incorrecta
        When ingresa el usuario 'standard_user' y la contreseña '12345'
        And hace clic en el boton Login
        Then deberia ver el mensaje de error 'Epic sadface: Username and password do not match any user in this service'
    
    @negativo @regression
    Scenario Outline: Login invalido con diferentes usuarios
        When ingresa el usuario '<usuario>' y la contreseña '<password>'
        And hace clic en el boton Login
        Then deberia ver el mensaje de error '<mensaje>'

        Examples:
            |usuario|password|mensaje|
            |standard_user|12345|Epic sadface: Username and password do not match any user in this service|
            |standart_user|secret_sauce|Epic sadface: Username and password do not match any user in this service|
            | VACIO | secret_sauce | Epic sadface: Username is required|
            | standard_user | VACIO | Epic sadface: Password is required|

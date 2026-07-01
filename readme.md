# Proyecto de Automatización QA - Maira Aguirre Gusmán

## Descripción

Framework de automatización de pruebas desarrollado en Python, que combina pruebas de interfaz (Selenium WebDriver) y pruebas de API (Requests) sobre patrones de diseño como Page Object Model. El objetivo es validar los flujos principales de la aplicación demo [SauceDemo](https://www.saucedemo.com) y de la API pública [ReqRes](https://reqres.in), generando reportes visuales y logs detallados de cada ejecución.

Trabajo Final Integrador de la Tecnicatura Universitaria en Programación - UTN.

## Tecnologías utilizadas

| Tecnología | Rol |
|---|---|
| Python | Lenguaje principal |
| Selenium WebDriver | Automatización de la interfaz web |
| Requests | Automatización de pruebas de API |
| Pytest | Framework de testing |
| pytest-html | Generación de reportes HTML |
| pytest-check | Assertions múltiples (soft asserts) sin cortar el test al primer fallo |
| webdriver-manager | Gestión automática del ChromeDriver |
| Behave | Pruebas BDD (Gherkin) para el flujo de login |
| Git / GitHub | Control de versiones |
| GitHub Actions | Integración continua (CI) |

## Estructura del proyecto

```
proyecto-final-automation-testing-Maira-Aguirre-Gusman/
│
├── .github/workflows/
│   └── tests.yml              # Workflow de GitHub Actions (corre en cada push a main)
│
├── data/
│   ├── users.csv              # Datos de usuarios para pruebas parametrizadas de login
│   └── products.json          # Datos de productos para pruebas parametrizadas de carrito
│
├── features/                  # Pruebas BDD (Behave) del flujo de login
│   ├── environment.py
│   ├── login.feature
│   └── steps/
│       └── login_steps.py
│
├── page/                      # Page Object Model
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── test/                      # Suite principal de tests (Pytest)
│   ├── test_login.py          # Login: caso válido e inválido
│   ├── test_login_csv.py      # Login parametrizado con datos externos (CSV)
│   ├── test_inventory.py      # Catálogo: título, productos, elementos de UI
│   ├── test_cart.py           # Carrito: agregar producto y verificar badge
│   ├── test_cart_json.py      # Carrito parametrizado con datos externos (JSON)
│   └── test_api.py            # Pruebas de API: GET, POST, DELETE sobre ReqRes
│
├── utils/
│   ├── data_reader.py         # Lectura de CSV y JSON
│   └── logger.py              # Configuración del sistema de logging
│
├── logs/                      # Logs generados en cada corrida (no se versiona)
├── reports/screenshots/       # Capturas automáticas de tests fallidos (no se versiona)
│
├── conftest.py                # Fixtures compartidas (driver, driver_logged) y hook de capturas
├── pytest.ini                 # Configuración de Pytest y markers
├── requirements.txt           # Dependencias del proyecto
└── report.html                # Último reporte HTML generado
```

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/mairaguirre/proyecto-final-automation-testing-Maira-Aguirre-Gusman.git
cd proyecto-final-automation-testing-Maira-Aguirre-Gusman
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si `pytest` no se reconoce como comando después de instalar, ejecutalo como módulo: `python -m pytest`.

## Ejecución de las pruebas

### Ejecutar toda la suite (UI + API) con reporte HTML

```bash
pytest
```

El reporte HTML se genera automáticamente en `report.html` gracias a la configuración de `pytest.ini` (no hace falta pasar flags adicionales).

### Ejecutar solo las pruebas de UI

```bash
pytest test/test_login.py test/test_login_csv.py test/test_inventory.py test/test_cart.py test/test_cart_json.py -v
```

### Ejecutar solo las pruebas de API

```bash
pytest test/test_api.py -v
```

### Ejecutar por markers

El proyecto define markers en `pytest.ini` para filtrar ejecuciones:

| Marker | Descripción |
|---|---|
| `smoke` | Pruebas críticas del sistema |
| `regression` | Pruebas de regresión |
| `api` | Pruebas de API |
| `ui` | Pruebas de interfaz |

```bash
pytest -m smoke -v
pytest -m api -v
```

### Ejecutar las pruebas BDD (Behave)

```bash
behave features/
```

## Cómo interpretar los reportes

### Reporte HTML (`report.html`)

Al finalizar la ejecución, abrí `report.html` en el navegador. Vas a encontrar:

- Un resumen con la cantidad de tests **pasados**, **fallados** y su **duración total**
- El detalle de cada test individual con su estado y tiempo de ejecución
- Para los tests de UI que fallan, una **captura de pantalla** embebida en el reporte, tomada automáticamente en el momento del fallo

### Capturas de pantalla (`reports/screenshots/`)

Cada vez que un test de UI falla, se guarda una captura en `reports/screenshots/` con el nombre del test y la fecha/hora del fallo (ej: `test_login_ok_01072026_154230.png`), para poder rastrear en qué momento exacto ocurrió.

### Logs (`logs/`)

Cada corrida genera un archivo `log_<fecha>_<hora>.log` con el detalle paso a paso de lo que hizo cada test (acciones realizadas, validaciones, respuestas de API, etc.). Es la primera fuente a revisar para depurar un fallo sin tener que volver a correr los tests con el navegador visible.

## Casos de prueba

### UI (Selenium)

| Archivo | Casos |
|---|---|
| `test_login.py` | Login exitoso / Login con contraseña inválida (negativo) |
| `test_login_csv.py` | Login parametrizado con múltiples combinaciones de usuario/contraseña (CSV) |
| `test_inventory.py` | Título de la página, productos visibles, elementos de UI (menú y filtro) |
| `test_cart.py` | Agregar producto y verificar contador del carrito |
| `test_cart_json.py` | Agregar múltiples productos desde datos externos (JSON) y validar contenido del carrito |

### API (Requests, sobre ReqRes)

| Archivo | Casos |
|---|---|
| `test_api.py` | Login válido (POST) / Login sin password (POST, negativo) / Login sin email (POST, negativo) / Crear usuario (POST) / Eliminar usuario (DELETE) / Obtener usuario (GET) |

## Integración continua (CI/CD)

El repositorio tiene configurado un workflow de GitHub Actions (`.github/workflows/tests.yml`) que se ejecuta automáticamente en cada `push` a la rama `main`:

1. Descarga el repositorio
2. Configura Python
3. Instala las dependencias
4. Ejecuta toda la suite de pruebas con `pytest`
5. Sube `report.html` como artefacto de la ejecución, descargable desde la pestaña **Actions** del repositorio

## Credenciales de prueba

Definidas como datos de prueba en `data/users.csv` y usadas en `page/login_page.py`:

```
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
```

> SauceDemo y ReqRes son sitios públicos de práctica. No se manejan datos reales.

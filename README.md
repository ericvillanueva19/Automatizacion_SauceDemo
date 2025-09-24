# Automatizacion_SauceDemo
SauceDemo web automation project in Selenium with Python and Unitests

Automatización SauceDemo (Selenium + Python + HtmlTestRunner)

Automatización web de SauceDemo
 enfocada en flujos clave de e-commerce: login, agregar al carrito, checkout y logout, además de casos de regresión y pruebas extra (ordenamiento, reset de estado, etc.).
El proyecto usa Selenium 4 con unittest y reportes HTML generados con HtmlTestRunner.

✨ Objetivos

Demostrar un flujo end-to-end estable y mantenible.

Organizar suites en Smoke, Regresión y Extras.

Generar reportes HTML profesionales para evidencia de ejecución.

🔧 Tecnologías

Python 3.11+

Selenium 4, webdriver-manager

unittest (estructura) + HtmlTestRunner (reportes HTML)

📂 Estructura del proyecto
Automatizacion_SauceDemo/
│
├─ tests/                         # Pruebas automatizadas
│  ├─ test_smoke_saucedemo.py     # Suite Smoke
│  ├─ test_regression_saucedemo.py# Suite Regresión
│  └─ test_extra_saucedemo.py     # Suite Extras
│
├─ utils/
│  └─ Funciones.py                # Funciones reutilizables (wrappers Selenium)
│
├─ reports/                       # Salida de reportes HTML (se genera al correr)
├─ runner.py                      # Orquestador: ejecuta tests + genera reporte
├─ requirements.txt               # Dependencias del proyecto
├─ .gitignore
└─ README.md

📦 Requisitos

Crea (o actualiza) requirements.txt con:

selenium
webdriver-manager
html-testRunner


Nota: el paquete se instala como html-testRunner (con guion) y se importa como HtmlTestRunner (CamelCase).

▶️ Cómo ejecutar el proyecto
1) Clonar e instalar dependencias
git clone <URL_DE_TU_REPO>.git
cd Automatizacion_SauceDemo

# (opcional pero recomendado) crear venv
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

2) Ejecutar todas las pruebas y generar reporte
python runner.py


El reporte se genera en: reports/reporte_unittest_YYYYMMDD_HHMMSS.html

Ábrelo en el navegador para ver el detalle (tests pasados/fallidos, tiempos, tracebacks).

3) Ejecutar una suite específica (opcional)
# Solo Smoke
python -m unittest -v tests.test_smoke_saucedemo

# Solo Regresión
python -m unittest -v tests.test_regression_saucedemo

# Solo Extras
python -m unittest -v tests.test_extra_saucedemo

🔐 Usuarios de prueba (SauceDemo)

standard_user / secret_sauce

locked_out_user / secret_sauce

performance_glitch_user / secret_sauce

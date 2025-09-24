import tempfile
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

t = 2
from Funciones import Funciones_Globales

class regresion_test(unittest.TestCase):

    def setUp(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        # 1) Modo invitado (perfil “vacío” sin contraseñas/Sync)
        options.add_argument("--guest")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-sync")
        options.add_argument("--disable-extensions")

        # 2) Preferencias que desactivan gestor/auto-signin/autofill
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "credentials_enable_autosignin": False,
            "autofill.profile_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        # 3) Desactivar features que disparan ese popup
        options.add_argument(
            "--disable-features="
            "PasswordLeakDetection,"
            "PasswordManagerOnboarding,"
            "AutofillServerCommunication,"
            "CredentialManagementAPI"
        )

        # (opcional) quitar banners de “automation”
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()

    def _cierra_popup_chrome(self):
        """Plan B: si aun así aparece, lo cerramos con ESC."""
        try:
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except Exception:
            pass
        # segundo intento con JS (algunas builds)
        try:
            self.driver.execute_script("""
                window.dispatchEvent(new KeyboardEvent('keydown', {key:'Escape'}));
                window.dispatchEvent(new KeyboardEvent('keyup', {key:'Escape'}));
            """)
        except Exception:
            pass

    def test1(self):  # SD-RG-01 - Login inválido (password incorrecto)
        f = Funciones_Globales(self.driver)
        # usa la URL nueva (evita /v1/)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath", "//input[@id='user-name']", "standard_user",2)
        f.Texto_Mixto("xpath", "//input[@id='password']", "hola1234",2)
        f.Click_Mixto("xpath", "//input[@id='login-button']", 4)

    def test2(self): #SD-RG-02 - Usuario bloqueado
        f = Funciones_Globales(self.driver)
        # usa la URL nueva (evita /v1/)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath", "//input[@id='user-name']", "locked_out_user",2)
        f.Texto_Mixto("xpath", "//input[@id='password']", "secret_sauce",2)
        f.Click_Mixto("xpath", "//input[@id='login-button']", 4)
    def test3(self):#SD-RG-03 - Campos requeridos en checkout (First Name vacío)

        f = Funciones_Globales(self.driver)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath", "//input[@id='user-name']", "standard_user")
        f.Texto_Mixto("xpath", "//input[@id='password']", "secret_sauce")
        f.Click_Mixto("xpath", "//input[@id='login-button']", 2)
        self._cierra_popup_chrome()
        f.Click_Mixto("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']", 1)
        f.Click_Mixto("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']", 1)
        f.Click_Mixto("xpath", "//a[@class='shopping_cart_link']", 4)
        f.Click_Mixto("xpath", "//button[@id='checkout']", 4)

        f.Texto_Mixto("xpath", "//input[@id='last-name']", "Villanueva", 3)
        f.Texto_Mixto("xpath", "//input[@id='postal-code']", "10100", 3)
        f.Click_Mixto("xpath", "//input[@id='continue']", 4)

    def test4(self): #SD-RG-04 - Remover producto del carrito
        f = Funciones_Globales(self.driver)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath", "//input[@id='user-name']", "standard_user")
        f.Texto_Mixto("xpath", "//input[@id='password']", "secret_sauce")
        f.Click_Mixto("xpath", "//input[@id='login-button']", 4)
        self._cierra_popup_chrome()
        f.Click_Mixto("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']", 4)
        f.Click_Mixto("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']", 4)
        f.Click_Mixto("xpath", "//a[@class='shopping_cart_link']", 4)
        f.Click_Mixto("xpath", "//button[@id='remove-sauce-labs-backpack']", 4)

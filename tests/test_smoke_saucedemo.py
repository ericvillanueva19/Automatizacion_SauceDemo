import tempfile
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

t = 2
from Funciones import Funciones_Globales

class smoke_test(unittest.TestCase):

    def setUp(self):
        # perfil temporal limpio
        tmp_profile = tempfile.mkdtemp()

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument(f"--user-data-dir={tmp_profile}")   # <- perfil limpio
        # options.add_argument("--guest")  # alternativa: modo invitado

        # Desactivar gestor/auto-sign-in y fugas
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "credentials_enable_autosignin": False,
            "autofill.profile_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,PasswordManagerOnboarding,CredentialManagementAPI,PasswordImport")
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

    def test1(self):  # SD-SM-01 - Login válido
        f  = Funciones_Globales(self.driver)
        # usa la URL nueva (evita /v1/)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath","//input[@id='user-name']","standard_user")
        f.Texto_Mixto("xpath","//input[@id='password']","secret_sauce")
        f.Click_Mixto("xpath","//input[@id='login-button']",4)

        # por si las moscas, cierra overlay si se coló
        self._cierra_popup_chrome()

    def test2(self):  # SD-SM-02 - Agregar 2 productos y verificar carrito
        f  = Funciones_Globales(self.driver)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath","//input[@id='user-name']","standard_user")
        f.Texto_Mixto("xpath","//input[@id='password']","secret_sauce")
        f.Click_Mixto("xpath","//input[@id='login-button']",4)
        self._cierra_popup_chrome()

        f.Click_Mixto("xpath","//button[@id='add-to-cart-sauce-labs-backpack']",4)
        f.Click_Mixto("xpath","//button[@id='add-to-cart-sauce-labs-bike-light']",4)
        f.Click_Mixto("xpath","//a[@class='shopping_cart_link']",4)

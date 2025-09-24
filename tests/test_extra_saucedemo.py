import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

t = 2
from Funciones import Funciones_Globales

class extra_test(unittest.TestCase):

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


    def test1(self):  #  SD-EX-01 - Ordenar por precio (low → high)
        f = Funciones_Globales(self.driver)
        # usa la URL nueva (evita /v1/)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath", "//input[@id='user-name']", "standard_user",2)
        f.Texto_Mixto("xpath", "//input[@id='password']", "secret_sauce",2)
        f.Click_Mixto("xpath", "//input[@id='login-button']", 4)
        f.Select_Xpath_Type("//select[@class='product_sort_container']", "index", 2, 10)
    def test2(self): # SD-EX-03 - Performance Glitch User
        f = Funciones_Globales(self.driver)
        # usa la URL nueva (evita /v1/)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("xpath", "//input[@id='user-name']", "performance_glitch_user", 2)
        f.Texto_Mixto("xpath", "//input[@id='password']", "secret_sauce", 2)
        f.Click_Mixto("xpath", "//input[@id='login-button']", 4)


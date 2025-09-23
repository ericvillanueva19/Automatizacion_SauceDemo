import unittest

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

t=2
from Funciones import Funciones_Globales

class flujo_completo(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless=new")  # opcional

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()



    def test1(self): #Prueba de login
        driver= self.driver
        f  = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/v1/",t)
        f.Texto_Mixto("xpath","//input[@id='user-name']","standard_user")
        f.Texto_Mixto("xpath", "//input[@id='password']", "secret_sauce")
        f.Click_Mixto("xpath","//input[@id='login-button']",4)
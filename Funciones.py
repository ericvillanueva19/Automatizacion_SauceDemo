# Funciones.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


class Funciones_Globales:

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.default_timeout = timeout

    # -------------------- helpers internos --------------------
    def _wait(self, seconds: int | float | None = None):
        if seconds:
            time.sleep(seconds)

    def _scroll_into_view(self, el):
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", el
            )
        except Exception:
            pass

    # find visible by XPATH
    def SEX(self, elemento: str, timeout: int | None = None):
        to = timeout or self.default_timeout
        el = WebDriverWait(self.driver, to).until(
            EC.visibility_of_element_located((By.XPATH, elemento))
        )
        self._scroll_into_view(el)
        return el

    # find selected by XPATH (útil para checks/radios ya seleccionados)
    def SEXS(self, elemento: str, timeout: int | None = None):
        to = timeout or self.default_timeout
        # En Selenium 4 existe element_located_to_be_selected
        WebDriverWait(self.driver, to).until(
            EC.element_located_to_be_selected((By.XPATH, elemento))
        )
        el = self.driver.find_element(By.XPATH, elemento)
        self._scroll_into_view(el)
        return el

    # find visible by ID
    def SEI(self, elemento: str, timeout: int | None = None):
        to = timeout or self.default_timeout
        el = WebDriverWait(self.driver, to).until(
            EC.visibility_of_element_located((By.ID, elemento))
        )
        self._scroll_into_view(el)
        return el

    # -------------------- acciones públicas --------------------
    def Tiempo(self, tie: float):
        time.sleep(tie)

    def Navegar(self, Url: str, Tiempo: float = 0):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: " + str(Url))
        self._wait(Tiempo)

    def Texto_Mixto(self, tipo: str, selector: str, texto: str, tiempo: float = 0.1):
        try:
            if tipo == "xpath":
                el = self.SEX(selector)
            elif tipo == "id":
                el = self.SEI(selector)
            else:
                raise ValueError(f"Tipo no soportado: {tipo}")

            el.clear()
            el.send_keys(texto)
            print(f"Escribiendo en el campo {selector} el texto -> {texto}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)

    def Click_Mixto(self, tipo: str, selector: str, tiempo: float = 0.1):
        try:
            if tipo == "xpath":
                el = self.SEX(selector)
            elif tipo == "id":
                el = self.SEI(selector)
            else:
                raise ValueError(f"Tipo no soportado: {tipo}")

            el.click()
            print(f"Dando click en {selector} -> {selector}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)

    def Salida(self):
        print("Se termina la prueba Exitosamente")

    # -------------------- selects --------------------
    def Select_Xpath_Type(self, xpath: str, tipo: str, dato, tiempo: float = 0.1):
        try:
            el = self.SEX(xpath)
            sel = Select(el)
            if tipo == "text":
                sel.select_by_visible_text(str(dato))
            elif tipo == "index":
                sel.select_by_index(int(dato))
            elif tipo == "value":
                sel.select_by_value(str(dato))
            else:
                raise ValueError("tipo debe ser 'text', 'index' o 'value'")
            print(f"El campo Seleccionado es {dato}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)

    def Select_ID_Type(self, id_: str, tipo: str, dato, tiempo: float = 0.1):
        try:
            el = self.SEI(id_)
            sel = Select(el)
            if tipo == "text":
                sel.select_by_visible_text(str(dato))
            elif tipo == "index":
                sel.select_by_index(int(dato))
            elif tipo == "value":
                sel.select_by_value(str(dato))
            else:
                raise ValueError("tipo debe ser 'text', 'index' o 'value'")
            print(f"El campo Seleccionado es {dato}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + id_)

    # -------------------- uploads --------------------
    def Upload_Xpath(self, xpath: str, ruta: str, tiempo: float = 0.1):
        try:
            el = self.SEX(xpath)  # (antes usaba ruta por error)
            el.send_keys(ruta)
            print(f"Se carga el archivo {ruta}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)

    def Upload_ID(self, id_: str, ruta: str, tiempo: float = 0.1):
        try:
            el = self.SEI(id_)  # (antes usaba ruta por error)
            el.send_keys(ruta)
            print(f"Se carga el archivo {ruta}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + id_)

    # -------------------- radio/check --------------------
    def Check_Xpath(self, xpath: str, tiempo: float = 0.1):
        try:
            el = self.SEX(xpath)
            el.click()
            print(f"Click en el elemento {xpath}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)

    def Check_ID(self, id_: str, tiempo: float = 0.1):
        try:
            el = self.SEI(id_)
            el.click()
            print(f"Click en el elemento {id_}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + id_)

    def Check_Xpath_Multiples(self, tiempo: float, *args):
        try:
            for num in args:
                el = self.SEX(num)
                el.click()
                print(f"Click en el elemento {num}")
                self._wait(tiempo)
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontró el elemento " + num)

    def Existe(self, tipo: str, selector: str, tiempo: float = 0.0):
        try:
            if tipo == "xpath":
                _ = self.SEX(selector)
            elif tipo == "id":
                _ = self.SEI(selector)
            else:
                raise ValueError(f"Tipo no soportado: {tipo}")
            print(f"El elemento {selector} -> existe")
            self._wait(tiempo)
            return "Existe"
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)
            return "No Existe"

    # -------------------- acciones de mouse --------------------
    def Mouse_Doble(self, tipo: str, selector: str, tiempo: float = 0.2):
        try:
            el = self.SEX(selector) if tipo == "xpath" else self.SEI(selector)
            ActionChains(self.driver).double_click(el).perform()
            print(f"DoubleClick en {selector}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)

    def Mouse_Derecho(self, tipo: str, selector: str, tiempo: float = 0.2):
        try:
            el = self.SEX(selector) if tipo == "xpath" else self.SEI(selector)
            ActionChains(self.driver).context_click(el).perform()
            print(f"ClickDerecho en {selector}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)

    def Mouse_DragDrop(self, tipo: str, selector: str, destino: str, tiempo: float = 0.2):
        try:
            el1 = self.SEX(selector) if tipo == "xpath" else self.SEI(selector)
            el2 = self.SEX(destino) if tipo == "xpath" else self.SEI(destino)
            ActionChains(self.driver).drag_and_drop(el1, el2).perform()
            print(f"Se soltó el elemento {selector}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)

    def Mouse_DragDropXY(self, tipo: str, selector: str, x: int, y: int, tiempo: float = 0.2):
        try:
            el = self.SEX(selector) if tipo == "xpath" else self.SEI(selector)
            ActionChains(self.driver).drag_and_drop_by_offset(el, x, y).perform()
            print(f"Se soltó el elemento {selector}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)

    def ClickXY(self, tipo: str, selector: str, x: int, y: int, tiempo: float = 0.2):
        try:
            el = self.SEX(selector) if tipo == "xpath" else self.SEI(selector)
            ActionChains(self.driver).move_to_element_with_offset(el, x, y).click().perform()
            print(f"Click al elemento {selector} coordenada {x}, {y}")
            self._wait(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + selector)





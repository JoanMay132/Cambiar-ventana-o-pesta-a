import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\Descargas\chromedriver_win32\chromedriver.exe") #ruta del driver

    def test_cambiar_ventana(self):
        driver=self.driver
        driver.get("https://www.google.com") #abrir el navegador
        time.sleep(3)
        driver.execute_script("window.open('')") #funcion python abre nueva pestaña
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) #posicionate en la pestaña 1 para cargar una pagina nueva
        driver.get("https://www.youtube.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0]) #despues de abrir el link anterior se regresa a la pestaña 0["google"]
        time.sleep(3)
if __name__=='__main__':
    unittest.main()
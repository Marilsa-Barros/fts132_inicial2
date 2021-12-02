# 1- Importar Bibliotecas / Pacotes

import pytest  # Framework de Teste de Unidade / Engine / Motor
import time  # Controle do Tempo
import json  # Ler e escrever no formato Json
from selenium import webdriver  # Bibliotecas do Selenium Webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestConsultarMantis2():
    def setup_method(self, method):
        # Instanciar o obejto do Selenium WebDriver como Chrome
        self.driver = webdriver.Chrome('C:/Users/Tata/PycharmProjects/fts132_inicial2/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30) # o robô irá esperar por até 30 segundos pelos elementos
        self.driver.maximize_window()   # Maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultarMantis2(self):
        self.driver.get("https://iterasys.com.br/")
        self.driver.set_window_size(797, 791)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("Mantis")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-search").click()
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".item-title").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        self.driver.find_element(By.CSS_SELECTOR, ".new-price").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"

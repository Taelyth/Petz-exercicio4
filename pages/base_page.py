from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _localizar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _clicar(self, locator):
        self._localizar(locator).click()

    def _escrever(self, locator, texto):
        self._localizar(locator).send_keys(texto)

    def _esperar_texto_elemento(self, locator, texto):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (locator['by'], locator['value']), texto))

    def _rolar(self, locator):
        elemento = self._localizar(locator)
        acao = ActionChains(self.driver)
        acao.move_to_element(elemento)
        acao.perform()

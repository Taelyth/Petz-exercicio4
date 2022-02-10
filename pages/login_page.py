from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class LoginPage(BasePage):
    sem_login_btn = {
        'by': AppiumBy.ID,
        'value': 'br.com.petz:id/tv_start_without_login'
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clicar_botao_sem_login(self):
        self.driver.implicitly_wait(5)
        self._clicar(self.sem_login_btn)

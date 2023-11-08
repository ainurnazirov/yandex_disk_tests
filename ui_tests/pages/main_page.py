from ui_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    URL = "http://yandex.ru/"
    LOGIN_BUTTON = (By.CLASS_NAME, 'login-button__iconButtonContainer-1C')
    LOGIN_VIA_YANDEX_ID_BUTTON = (By.CLASS_NAME, 'login-content__yaButtonWrapper-15')

    def open(self):
        self.driver.get(self.URL)

    def go_to_login_page(self):
        self.click_element(self.LOGIN_BUTTON)
        self.click_element(self.LOGIN_VIA_YANDEX_ID_BUTTON)

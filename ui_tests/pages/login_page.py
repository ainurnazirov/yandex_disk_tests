from ui_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_INPUT = (By.ID, 'passp-field-login')
    LOGIN_PASSWORD_BUTTON = (By.ID, 'passp:sign-in')
    PASSWORD_INPUT = (By.ID, 'passp-field-passwd')
    USER_ICON = (By.CLASS_NAME, 'content-desktop__profileMenu-1J')

    def login(self, username, password):
        self.enter_text(self.LOGIN_INPUT, username)
        self.click_element(self.LOGIN_PASSWORD_BUTTON)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_PASSWORD_BUTTON)
        self.get_element(self.USER_ICON)
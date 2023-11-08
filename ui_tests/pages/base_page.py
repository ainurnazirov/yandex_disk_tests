from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_elements(self, locator, timeout=10):
        self.driver.implicitly_wait(timeout)
        return self.driver.find_elements(*locator)

    def enter_text(self, locator, text, timeout=10):
        element = self.get_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator, timeout=10):
        element = self.get_element(locator, timeout)
        element.click()

    def double_click_element(self, locator, timeout=10):
        element = self.get_element(locator, timeout)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

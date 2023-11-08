from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DiskPage(BasePage):
    URL = 'https://disk.yandex.ru/'
    CREATE_BUTTON = (By.CLASS_NAME, 'create-resource-popup-with-anchor')
    FOLDER_BUTTON = (By.XPATH, "//button[@class='create-resource-button "
                               "create-resource-popup-with-anchor__create-item' and @aria-label='Папку']")
    FILE_BUTTON = (By.XPATH, "//button[@class='create-resource-button create-resource-popup-with-anchor__create-item' "
                             "and @aria-label='Текстовый документ']")
    FOLDER_NAME_INPUT = (By.XPATH, "//input[@class='Textinput-Control' and @value='Новая папка']")
    FILE_NAME_INPUT = (By.XPATH, "//input[@class='Textinput-Control' and @value='Новый документ']")
    SAVE_BUTTON = (By.CLASS_NAME, 'confirmation-dialog__button')
    FOLDER = (By.XPATH, "//div[@class='listing-item__title listing-item__title_overflow_clamp' and @aria-label='{}']")
    FILES = (By.CLASS_NAME, 'listing-item__title')
    PROFILE_ICON = (By.CLASS_NAME, 'PSHeader-User')
    LOGOUT_BUTTON = (By.XPATH, "//span[@class='menu__text' and contains(text(),'Выйти')]")

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    def create_name_folder(self, folder_name):
        self.click_element(self.CREATE_BUTTON)
        self.click_element(self.FOLDER_BUTTON)
        self.click_element(self.FOLDER_NAME_INPUT)
        element = self.get_element(self.FOLDER_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, '')
        element.send_keys(folder_name)
        self.click_element(self.SAVE_BUTTON)

    def open_folder(self, folder_name):
        self.double_click_element((self.FOLDER[0], self.FOLDER[1].format(folder_name)))

    def create_name_file(self, file_name):
        self.click_element(self.CREATE_BUTTON)
        self.click_element(self.FILE_BUTTON)
        self.click_element(self.FILE_NAME_INPUT)
        element = self.get_element(self.FILE_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, '')

        element.clear()
        element.send_keys(file_name)
        self.click_element(self.SAVE_BUTTON)

    def close_new_page(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.close()
        self.driver.switch_to.window(handles[0])

    def get_file_names(self):
        file_elements = self.get_elements(self.FILES)
        file_names = [element.text.replace('\n', '') for element in file_elements]
        return file_names

    def logout(self):
        self.click_element(self.PROFILE_ICON)
        self.click_element(self.LOGOUT_BUTTON)
import logging
import time
import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from ui_tests.pages.main_page import MainPage
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.disk_page import DiskPage
from utils.string_util import StringUtil

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


@pytest.fixture
def login():
    load_dotenv()
    return os.environ.get('YANDEX_ID_LOGIN')


@pytest.fixture
def password():
    load_dotenv()
    return os.environ.get('YANDEX_ID_PASSWORD')


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 700)
    yield driver

    driver.quit()


class TestUI:
    def test_create_folder_and_file(self, browser, login, password):
        folder_name = StringUtil.generate_random_string()
        file_name = StringUtil.generate_random_string()
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        disk_page = DiskPage(browser)

        main_page.open()
        # time.sleep(10)
        main_page.go_to_login_page()
        logger.info("Authorization")
        login_page.login(login, password)
        disk_page.open()
        logger.info(f"Creating folder: {folder_name}")
        disk_page.create_name_folder(folder_name)
        disk_page.open_folder(folder_name)
        logger.info(f"Creating file: {file_name}")
        disk_page.create_name_file(file_name)
        disk_page.close_new_page()
        file_names = disk_page.get_file_names()
        assert file_name + '.docx' in file_names
        disk_page.logout()

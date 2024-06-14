from selenium import webdriver
import pytest
import os
import shutil

from pages.login_page import LoginPage

USER_NAME = 'Anna'
INVALID_USER_NAME = 'Anna1'
PASSWORD = '12345'
INVALID_PASSWORD = '12346'


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser


@pytest.fixture()
def browser_doc():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser


@pytest.fixture()
def login(browser):
    """
    Фикстура для авторизации пользователя.
    Возвращает залогиненного пользователя.
    """
    url = 'http://192.168.102.120:8080/login'
    browser.get(url)

    login_page = LoginPage(browser)
    login_page.enter_username(USER_NAME)
    login_page.enter_password(PASSWORD)
    login_page.submit_button_click()
    return browser


# @pytest.fixture(scope="session")
# def clear_directory(directory_path):
#     """
#     Удаляет все файлы и подпапки в указанной директории.
#
#     :param directory_path: Путь к директории, которую нужно очистить.
#     """
#     if os.path.exists(directory_path):
#         for filename in os.listdir(directory_path):
#             file_path = os.path.join(directory_path, filename)
#             try:
#                 if os.path.isfile(file_path) or os.path.islink(file_path):
#                     os.unlink(file_path)
#                 elif os.path.isdir(file_path):
#                     shutil.rmtree(file_path)
#             except Exception as e:
#                 print(f'Не удалось удалить {file_path}. Причина: {e}')
#     else:
#         print(f'Директория {directory_path} не существует.')
#
# clear_directory('allure_results')

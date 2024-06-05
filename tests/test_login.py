from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium import webdriver
from time import sleep
import allure

USER_NAME = 'Anna'
INVALID_USER_NAME = 'Anna1'
PASSWORD = '12345'
INVALID_PASSWORD = '12346'


@allure.feature('Login')
@allure.story('Check error message about invalid user name / password')
def test_login_with_invalid_user_name(browser):
    login_page = LoginPage(browser)
    with allure.step('Open the page'):
        login_page.open()
    with allure.step(f'Enter invalid user name {INVALID_USER_NAME}'):
        login_page.enter_username(INVALID_USER_NAME)
    with allure.step(f'Enter password {PASSWORD}'):
        login_page.enter_password(PASSWORD)
    with allure.step('Click submit button'):
        login_page.submit_button_click()
    with allure.step('Check error message about invalid user name'):
        login_page.error_message()


@allure.feature('Login')
@allure.story('Check error message about invalid user name / password')
def test_login_with_invalid_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username(USER_NAME)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_username_field()
    login_page.submit_button_click()
    login_page.error_message()


@allure.feature('Login')
@allure.story('Check error label about empty user name / password')
def test_login_empty_user_name(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username("")
    login_page.enter_password(PASSWORD)
    login_page.submit_button_click()
    login_page.check_error_line_empty_user_name()


@allure.feature('Login')
@allure.story('Check error label about empty user name / password')
def test_login_empty_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username(USER_NAME)
    login_page.enter_password("")
    login_page.submit_button_click()
    login_page.check_error_line_empty_password()


@allure.feature('Login')
@allure.story('Check error label about empty user name / password')
def test_login_empty_user_and_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.submit_button_click()
    login_page.check_error_line_empty_user_name()
    login_page.check_error_line_empty_password()


@allure.feature('Login')
@allure.story('check successful login')
def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username(USER_NAME)
    login_page.enter_password(PASSWORD)
    assert login_page.submit_button_is_displayed()
    login_page.submit_button_click()
    sleep(1)
    with allure.step('Validate Startseite label on the Dashboard page'):
        assert "Startseite" in login_page.browser.page_source



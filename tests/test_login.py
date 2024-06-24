from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium import webdriver
from time import sleep
import allure

USER_NAME = 'Anna'
INVALID_USER_NAME = 'Anna1'
PASSWORD = '12345678'
INVALID_PASSWORD = '12346'


@allure.feature('Login')
@allure.story('Check floating line in user name and password fields')
def test_login_check_floating_line_in_username_password_fields(browser):
    login_page: LoginPage = LoginPage(browser)
    login_page.open()
    login_page.submit_button_click()
    login_page.username_field_click()
    with allure.step('Check red line in the empty user name field'):
        assert "Die Eingabe eines Benutzernamens erforderlich" in login_page.red_line_user_name().text
    login_page.password_field_click()
    with allure.step('Check red line in the empty password field'):
        assert "Die Eingabe eines Passwortes erforderlich" in login_page.red_line_password().text


@allure.feature('Login')
@allure.story('Check common error message about invalid user name / password')
def test_login_check_common_err_message_when_invalid_user_name_password(browser):
    login_page: LoginPage = LoginPage(browser)
    login_page.open()
    login_page.enter_username(INVALID_USER_NAME)
    login_page.enter_password(PASSWORD)
    login_page.submit_button_click()
    with allure.step('Check error message about invalid user name'):
        login_page.check_error_message()
    login_page.enter_username(USER_NAME)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.username_field_click()
    login_page.submit_button_click()
    with allure.step('Check error message about invalid password'):
        login_page.check_error_message()


@allure.feature('Login')
@allure.story('Check error label when empty user name / password')
def test_login_check_label_when_empty_user_name(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username("")
    login_page.enter_password(PASSWORD)
    login_page.submit_button_click()
    with allure.step(f'Check error label when empty user name: {login_page.check_error_label_empty_user_name().text}'):
        assert 'Die Eingabe eines Benutzernamens erforderlich' in login_page.check_error_label_empty_user_name().text


@allure.feature('Login')
@allure.story('Check error label when empty user name / password')
def test_login_check_label_when_empty_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username(USER_NAME)
    login_page.enter_password("")
    login_page.submit_button_click()
    with allure.step(f'Check error label about empty password: {login_page.check_error_label_empty_password().text}'):
        assert 'Die Eingabe eines Passwortes erforderlich' in login_page.check_error_label_empty_password().text
        # print(f' TEST TEXT  = {login_page.check_error_line_empty_user_name().text}')


@allure.feature('Login')
@allure.story('Check error label when empty user name / password')
def test_login_check_label_when_empty_user_and_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.submit_button_click()
    with allure.step(f'Check error label when empty user name: {login_page.check_error_label_empty_user_name().text}'):
        assert 'Die Eingabe eines Benutzernamens erforderlich' in login_page.check_error_label_empty_user_name().text
        assert 'Die Eingabe eines Passwortes erforderlich' in login_page.check_error_label_empty_password().text


@allure.feature('Login')
@allure.story('Check successful login')
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



from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium import webdriver
from time import sleep

USER_NAME = 'Anna'
WRONG_USER_NAME = 'Anna1'
PASSWORD = '12345'
WRONG_PASSWORD = '12346'


def test_check_messages_with_wrong_data_for_authorization(browser):
    # check login with wrong user_name
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_username(WRONG_USER_NAME)
    login_page.enter_password(PASSWORD)
    login_page.login_button_click()
    login_page.error_message()

    # check login with wrong password
    login_page.enter_username(USER_NAME)
    login_page.enter_password(WRONG_PASSWORD)
    login_page.click_username_field()
    login_page.login_button_click()
    login_page.error_message()

    # check login with empty user_name
    login_page.enter_username("")
    login_page.enter_password(PASSWORD)
    login_page.click_username_field()
    login_page.login_button_click()
    login_page.check_error_line_empty_user_name()

    # check login with empty password
    login_page.enter_username(USER_NAME)
    login_page.enter_password("")
    login_page.click_username_field()
    login_page.login_button_click()
    login_page.check_error_line_empty_password()

    # check login with empty user_name and password
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_username_field()
    login_page.login_button_click()
    login_page.check_error_line_empty_user_name()
    login_page.check_error_line_empty_password()

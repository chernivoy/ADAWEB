from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium import webdriver
from time import sleep

USER_NAME = 'Anna'
WRONG_USER_NAME = 'Anna1'
PASSWORD = '12345'
WRONG_PASSWORD = '12346'


# def error_message(self):
#     try:
#         tooltip = WebDriverWait(self.browser, 3).until(
#             EC.visibility_of_element_located(wrong_user_name_or_password_message_locator))
#         if tooltip.text:
#             print(f'\n Info line was found" {tooltip.text}"')
#         else:
#             print("Всплывающая подсказка появилась, но текста нет.")
#     except TimeoutException:
#         print("Всплывающая подсказка не появилась вовремя.")
#
#     except NoSuchElementException:
#         print("Всплывающая подсказка не найдена.")

#
# def check_error_line_empty_user_name2(self):
#     try:
#         locator = self.find(empty_user_name_error_line_locator)
#         print(f' Info tooltip was found "{empty_user_name_error_line_locator}"')
#         return locator
#     except Exception as e:
#         # Обработка исключения
#         print(f"Произошла ошибка: {e}")

def wait_error_line(self):
    try:
        # Явное ожидание появления всплывающей подсказки
        tooltip = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(empty_password_error_line_locator)
        )
        # Работа с всплывающей подсказкой
        print("Всплывающая подсказка появилась: ", tooltip.text)
    except Exception as e:
        print("Всплывающая подсказка не появилась: ", e)
    finally:
        self.browser.quit()
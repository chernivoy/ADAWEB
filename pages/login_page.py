from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


txt_username_locator = (By.XPATH, "//input[@type='text']")
txt_password_locator = (By.XPATH, "//input[@type='password']")
btn_submit_locator = (By.XPATH, "//span[@class='dx-button-text']")
url = 'http://192.168.102.120:8080/login?returnUrl=%2F'

empty_user_name_error_line_locator = (By.XPATH, "//div[@class='dx-item-content dx-validationsummary-item-content'][contains(text(), 'Die Eingabe eines Benutzernamens erforderlich')]")
empty_password_error_line_locator = (By.XPATH,"//div[@class='dx-overlay-content dx-invalid-message-content'][contains(text(), 'Die Eingabe eines Passwortes erforderlich')]")

wrong_user_name_message_locator = (By.XPATH, "//div[contains(text(),'Stellen Sie sicher, dass Benutzername und Passwort korrekt angegeben wurden')]")


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url)

    def enter_username(self, username):
        self.enter_text(username,txt_username_locator)

    def enter_password(self, password):
        self.enter_text(password, txt_password_locator)

    def button(self):
        return self.find(btn_submit_locator)

    def click_username_field(self):
        return self.click(txt_username_locator)

    def login_button_click(self):
        return self.find(btn_submit_locator).click()

    def login_button_is_displayed(self):
        return self.button().is_displayed()

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

    def check_error_line_empty_user_name(self):
        try:
            locator = self.find(empty_user_name_error_line_locator)
            print(f' Info tooltip was found "{empty_user_name_error_line_locator}"')
            return locator
        except Exception as e:
            # Обработка исключения
            print(f"Произошла ошибка: {e}")

    def check_error_line_empty_password(self):
        try:
            locator = self.find(empty_password_error_line_locator)
            print(f' Info tooltip was found {empty_password_error_line_locator}')
            return locator
        except Exception as e:
            # Обработка исключения
            print(f"Произошла ошибка: {e}")

    def error_message(self):
        try:
            tooltip = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(wrong_user_name_message_locator))
            if tooltip.text:
                print(f'\n Info line was found" {tooltip.text}"')
            else:
                print("Всплывающая подсказка появилась, но текста нет.")
        except TimeoutException:
            print("Всплывающая подсказка не появилась вовремя.")

        except NoSuchElementException:
            print("Всплывающая подсказка не найдена.")





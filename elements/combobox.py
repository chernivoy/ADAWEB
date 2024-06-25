import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ComboBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def select_by_value(self, locator, value):
        with allure.step('Select data in combobox by text'):
            combobox = self.find(locator)
            combobox.click()
            wait = WebDriverWait(self.browser, 10)
            item_xpath = f"//div[contains(@class, 'dx-list-item')]//div[text()='{value}']"
            wait.until(EC.presence_of_element_located((By.XPATH, item_xpath)))
            item = self.browser.find_element(By.XPATH, item_xpath)
            item.click()

    def select_by_index(self, locator, index):
        # Поиск выпадающего списка по XPath и открытие его
        combobox = self.find(locator)
        combobox.click()

        # Явное ожидание появления элементов списка
        wait = WebDriverWait(self.browser, 10)
        items_xpath = "//div[contains(@class, 'dx-list-item')]"
        wait.until(EC.presence_of_all_elements_located((By.XPATH, items_xpath)))

        # Поиск всех элементов списка
        items = self.browser.find_elements(By.XPATH, items_xpath)

        # Проверка, что индекс находится в пределах допустимого диапазона
        if index < 0 or index >= len(items):
            raise IndexError(f"Индекс {index} вне диапазона. Допустимые значения: 0-{len(items) - 1}")

        # Выбор элемента по индексу и клик по нему
        item_to_select = items[index]
        item_to_select.click()
        return item_to_select.text

    def find_text(self, cmb_locator, cmb_dx_item_locator, text):
        with allure.step('Find data in combobox by text'):
            try:
                element = self.find(cmb_locator)
                element.click()
                items = element.find_elements(*cmb_dx_item_locator)

                matching_items = [item for item in items if item.text in text]

                if not matching_items:
                    with allure.step(f"Text '{text}' not found in the combobox."):
                        raise ValueError(f"Text '{text}' not found in the combobox.")

                if len(matching_items) == 1:
                    with allure.step(f"Text '{matching_items[0].text}' was found in the combobox."):
                        return matching_items[0].text

                matching_list = [item.text for item in matching_items]
                with allure.step(f"Text '{matching_list}' was found many times the combobox."):
                    return matching_list
            except ValueError as e:
                print(e)
                return None
            finally:
                element.click()  # Закрываем выпадающий список в любом случае

    # def validate_by_text(self, locator, value):
    #     selected_value = self.browser.find_element(By.XPATH, locator).text
    #     assert selected_value == value

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ComboBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def select_by_text(self, locator, value):
        with allure.step('Select data in combobox by text'):
            combobox = self.find(locator)
            combobox.click()
            wait = WebDriverWait(self.browser, 10)
            item_xpath = f"//div[contains(@class, 'dx-list-item')]//div[text()='{value}']"
            wait.until(EC.presence_of_element_located((By.XPATH, item_xpath)))
            item = self.browser.find_element(By.XPATH, item_xpath)
            item.click()












    # def validate_by_text(self, locator, value):
    #     selected_value = self.browser.find_element(By.XPATH, locator).text
    #     assert selected_value == value

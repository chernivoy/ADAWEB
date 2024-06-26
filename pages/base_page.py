import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_old(self, args):
        with allure.step('Find element'):
            return self.browser.find_element(*args)

    def find(self, locator):
        with allure.step('Find element'):
            try:
                element = WebDriverWait(self.browser, 2).until(
                    EC.presence_of_element_located(locator)
                )
                return element
            except (NoSuchElementException, TimeoutException):
                print(f"Element with args {locator} not found after 10 seconds")
                return None

    def find_elements(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_all_elements_located(locator))

    def find_elements_2(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_all_elements_located(*locator))

    def enter_text(self, text, *locator):
        element = self.find(*locator)
        element.clear()
        element.send_keys(text)

    def element_is_visible(self, locator, timeout=2):
        with allure.step('Check visibility element on the form'):
            try:
                return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                return False

    def elements_are_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=2):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element(locator))

    def element_is_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    # def go_to_element(self, element):
    #     self.browser.execute_script("argument[0].scrollInfoView();", element)

    def click(self, *locator):
        element = self.find(*locator)
        element.click()

    def text_box_get_value(self, locator):
        try:
            element = self.find(locator)
            value_txt_box = element.get_attribute("value")
            return value_txt_box
        except NoSuchElementException:
            return None





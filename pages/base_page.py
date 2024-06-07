import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        with allure.step('Find element'):
            return self.browser.find_element(*args)

    def enter_text(self, text, *locator):
        element = self.find(*locator)
        element.clear()
        element.send_keys(text)

    def element_is_visible(self, locator, timeout=10):
        with allure.step('Check visibility element on the form'):
            try:
                return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                return False

    def elements_are_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def enter_text(self, text, *locator):
        element = self.find(*locator)
        element.clear()
        element.send_keys(text)

    def find_elements(self, *locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(locator))

    def click(self, *locator):
        element = self.find(*locator)
        element.click()

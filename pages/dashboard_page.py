from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

btn_chevronleft_locator = (By.XPATH, "//dx-button[@icon='chevronleft' and @role='button']")
btn_preferences_locator = (By.XPATH, "//dx-button[@icon='preferences' and @role='button']")

btn_abmelden_locator = (By.XPATH, "//div[@role='button' and @aria-label='Abmelden' and contains(@class, 'dx-button-danger')]")
btn_conf_locator = (By.XPATH, "//div[@role='button' and @aria-label ='Konfiguration' and contains(@class, 'dx-widget dx-button dx-button-mode-outlined dx-button-normal dx-button-has-text')]")
btn_cansel_locator = (By.XPATH, "//div[@role='button' and @aria-label ='Abbrechen' and contains(@class, 'dx-widget dx-button dx-button-mode-outlined dx-button-normal dx-button-has-text')]")
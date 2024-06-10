from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure


url = 'http://192.168.102.120:8080'
btn_chevronleft_locator = (By.XPATH, "//dx-button[@icon='chevronleft' and @role='button']")
btn_preferences_locator = (By.XPATH, "//dx-button[@icon='preferences' and @role='button']")

btn_abmelden_locator = (By.XPATH, "//div[@role='button' and @aria-label='Abmelden' and contains(@class, 'dx-button-danger')]")
btn_conf_locator = (By.XPATH, "//div[@role='button' and @aria-label ='Konfiguration' and contains(@class, 'dx-widget dx-button dx-button-mode-outlined dx-button-normal dx-button-has-text')]")
btn_cansel_locator = (By.XPATH, "//div[@role='button' and @aria-label ='Abbrechen' and contains(@class, 'dx-widget dx-button dx-button-mode-outlined dx-button-normal dx-button-has-text')]")

lbl_Dashboard = (By.XPATH, "//p[contains(text(), 'Dashboard')]")
area_my_tasks = (By.CSS_SELECTOR, "ada-sub-category-button#scbMyTasks")


class DashboardPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step(f'Open page:{url}'):
            self.browser.get(url)

    def label_dashboard_click(self):
        with allure.step(f'Click on the dashboard label'):
            return self.click(lbl_Dashboard)

    def label_dashboard(self):
        return self.find(lbl_Dashboard)

    def label_dashboard_is_displayed(self):
        with allure.step(f'Check visibility dashboard label'):
            return self.label_dashboard().is_displayed()

    def area_my_tasks_click(self):
        return self.click(area_my_tasks)

    def my_tasks_count(self):
        with allure.step(f'Check my tasks count'):
            try:
                # Ищем контейнер с id="scbMyTasks"
                container = self.browser.find_element(By.CSS_SELECTOR, "ada-sub-category-button#scbMyTasks")
            except NoSuchElementException:
                print("Контейнер с id='scbMyTasks' не найден на странице")
            try:
                # Ищем элемент внутри контейнера, содержащий количество задач
                task_count_element = container.find_element(By.CSS_SELECTOR, "div.ng-star-inserted")
                # Извлекаем текст из элемента и преобразуем его в число
                task_count = int(task_count_element.text)
            except NoSuchElementException:
                print("Элемент с количеством задач не найден внутри контейнера")
                # Печатаем количество задач (для отладки)
            print(f"Count of my tasks : {task_count}")
            assert task_count > 0
            return task_count

    def given_tasks_count(self):
        with allure.step(f'Check my given tasks count'):
            try:
                # Ищем контейнер с id="scbGivenTasks"
                container = self.browser.find_element(By.CSS_SELECTOR, "ada-sub-category-button#scbGivenTasks")
            except NoSuchElementException:
                print("Контейнер с id='scbGivenTasks' не найден на странице")
            try:
                # Ищем элемент внутри контейнера, содержащий количество задач
                task_count_element = container.find_element(By.CSS_SELECTOR, "div.ng-star-inserted")
                # Извлекаем текст из элемента и преобразуем его в число
                task_count = int(task_count_element.text)
            except NoSuchElementException:
                print("Элемент с количеством задач не найден внутри контейнера")
                # Печатаем количество задач (для отладки)
            print(f"Count of given tasks : {task_count}")
            assert task_count > 0
            return task_count

    def created_tasks_count(self):
        with allure.step(f'Check my created tasks count'):
            try:
                # Ищем контейнер с id="scbCreatedTasks"
                container = self.browser.find_element(By.CSS_SELECTOR, "ada-sub-category-button#scbCreatedTasks")
            except NoSuchElementException:
                print("Контейнер с id='scbCreatedTasks' не найден на странице")
            try:
                # Ищем элемент внутри контейнера, содержащий количество задач
                task_count_element = container.find_element(By.CSS_SELECTOR, "div.ng-star-inserted")
                # Извлекаем текст из элемента и преобразуем его в число
                task_count = int(task_count_element.text)
            except NoSuchElementException:
                print("Элемент с количеством задач не найден внутри контейнера")
                # Печатаем количество задач (для отладки)
            print(f"Count of created tasks : {task_count}")
            assert task_count > 0
            return task_count

    def watched_tasks_count(self):
        with allure.step(f'Check my watched tasks count'):
            try:
                # Ищем контейнер с id="scbWatchedTasks"
                container = self.browser.find_element(By.CSS_SELECTOR, "ada-sub-category-button#scbWatchedTasks")
            except NoSuchElementException:
                print("Контейнер с id='scbWatchedTasks' не найден на странице")
            try:
                # Ищем элемент внутри контейнера, содержащий количество задач
                task_count_element = container.find_element(By.CSS_SELECTOR, "div.ng-star-inserted")
                # Извлекаем текст из элемента и преобразуем его в число
                task_count = int(task_count_element.text)
            except NoSuchElementException:
                print("Элемент с количеством задач не найден внутри контейнера")
                # Печатаем количество задач (для отладки)
            print(f"Count of watched tasks : {task_count}")
            assert task_count > 0
            return task_count

    def favorite_tasks_count(self):
        with allure.step(f'Check my favorite tasks count'):
            try:
                # Ищем контейнер с id="cbFavorites"
                container = self.browser.find_element(By.CSS_SELECTOR, "ada-category-button#cbFavorites")
            except NoSuchElementException:
                print("Контейнер с id='cbFavorites' не найден на странице")
            try:
                # Ищем элемент внутри контейнера, содержащий количество задач
                task_count_element = container.find_element(By.XPATH, ".//div[contains(@class, 'text-2xl') and contains(@class, 'ng-star-inserted')]")
                # Извлекаем текст из элемента и преобразуем его в число
                task_count = int(task_count_element.text)
            except NoSuchElementException:
                print("Элемент с количеством задач не найден внутри контейнера")
                # Печатаем количество задач (для отладки)
            print(f"Count of watched tasks : {task_count}")
            assert task_count > 0
            return task_count

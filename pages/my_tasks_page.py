from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure


url = 'http://192.168.102.120:8080/tasks/my'
data_grid_empty_locator = (By.XPATH, "//div[@class='dx-datagrid-rowsview dx-scrollable dx-visibility-change-handler dx-scrollable-both dx-scrollable-simulated dx-empty']")
data_grid_locator = (By.XPATH, "//div[@class='dx-datagrid-rowsview dx-scrollable dx-visibility-change-handler dx-scrollable-both dx-scrollable-simulated']")
search_field_locator = (By.XPATH, "//input[@aria-label='Suchen in der Datentabelle']")


class MyTasksPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def table_contains_text_old(self, value):
        with allure.step(f'Find "{value}" value in the table by text in cell'):
            is_bool = self.label_data_grid_empty_locator_is_visible()
            if not is_bool:
                table = self.find(data_grid_locator)
                is_find_element = False
                rows = table.find_elements(By.TAG_NAME, 'tr')
                # # Traverse each row
                for row in rows:
                    # Fetch the columns from a particular row
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    if len(cells) > 0:
                        # Traverse each column
                        for cell in cells:
                            if cell.text == value:
                                try:
                                    print(f"Value in row : '{cell.text}' was clicked.")
                                    cell.click()
                                    is_find_element = True
                                except Exception as e:
                                    print(f"Exception occurred: {e}")
                                break
                    else:
                        # To print the data into the console
                        print("This is Header Row")
                        print(rows[0].text.replace(" ", "\t\t"))
                    if is_find_element:
                        break
                if not is_find_element:
                    with allure.step(f"Value '{value}' was not found in the table after checking all cells"):
                        print(f"Value '{value}' was not found in the table after checking all cells")
            else:
                with allure.step(f'table was not present or empty'):
                    print("table was not present or empty")

    def table_contains_text(self, value):
        with allure.step(f'Find "{value}" value in the table by text in cell'):
            if self.label_data_grid_empty_locator_is_visible():
                with allure.step('Table was not present or empty'):
                    print("Table was not present or empty")
                return

            table = self.find(data_grid_locator)
            is_find_element = False

            # Обход строк таблицы
            for row in table.find_elements(By.TAG_NAME, 'tr'):
                # Получение ячеек из строки
                cells = row.find_elements(By.TAG_NAME, 'td')

                if not cells:
                    # Печать данных заголовка в консоль
                    print("This is Header Row")
                    print(row.text.replace(" ", "\t\t"))
                    continue

                # Обход ячеек в строке
                for cell in cells:
                    if cell.text == value:
                        try:
                            print(f"Value in row : '{cell.text}' was clicked.")
                            cell.click()
                            is_find_element = True
                        except Exception as e:
                            print(f"Exception occurred: {e}")
                        break

                if is_find_element:
                    break

            if not is_find_element:
                with allure.step(f"Value '{value}' was not found in the table after checking all cells"):
                    print(f"Value '{value}' was not found in the table after checking all cells")

    def search_field_click(self):
        with allure.step(f'Click in the search field'):
            return self.click(search_field_locator)

    def search_field_enter_text(self, value):
        with allure.step(f'Enter "{value}" value in search field '):
            self.enter_text(value, search_field_locator)

    def label_data_grid_locator_is_visible(self):
        return self.element_is_visible(data_grid_locator)

    def label_data_grid_empty_locator_is_visible(self):
        return self.element_is_visible(data_grid_empty_locator)

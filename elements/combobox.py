import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep



class ComboBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def select_by_value_old(self, locator, value):
        with allure.step('Select data in combobox by text'):
            combobox = self.find(locator)
            combobox.click()
            wait = WebDriverWait(self.browser, 10)
            item_xpath = f"//div[contains(@class, 'dx-list-item')]//div[text()='{value}']"
            wait.until(EC.presence_of_element_located((By.XPATH, item_xpath)))
            wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
            item = self.browser.find_element(By.XPATH, item_xpath)
            item.click()

    def select_by_value_old(self, locator, value):
        with allure.step('Select data in combobox by text'):
            combobox = self.find(locator)
            combobox_id = combobox.get_attribute('id')
            combobox.click()
            wait = WebDriverWait(self.browser, 10)
            item_xpath = f"//div[contains(@class, 'dx-list-item')]//div[text()='{value}']"
            wait.until(EC.presence_of_element_located((By.XPATH, item_xpath)))

            def click_with_check(element):
                try:
                    # Ensure the element is clickable
                    wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
                    element.click()
                    return True
                except ElementClickInterceptedException:
                    return False
                except (TimeoutException, StaleElementReferenceException):
                    return False

            item = self.browser.find_element(By.XPATH, item_xpath)
            is_clicked = click_with_check(item)

            if not is_clicked:
                # Scroll to the element and try clicking again
                self.browser.execute_script("arguments[0].scrollIntoView(true);", item)
                sleep(1)  # Optional: Add a delay if needed
                is_clicked = click_with_check(item)

            if not is_clicked:
                # Try clicking using JavaScript
                self.browser.execute_script("arguments[0].click();", item)
                sleep(1)  # Optional: Add a delay if needed
                is_clicked = click_with_check(item)

            if not is_clicked:
                # Try clicking using Actions
                actions = ActionChains(self.browser)
                actions.move_to_element(item).click().perform()
                sleep(1)  # Optional: Add a delay if needed
                is_clicked = click_with_check(item)

            if not is_clicked:
                # Check visibility and enabled state
                if item.is_displayed() and item.is_enabled():
                    # Retry clicking
                    sleep(1)
                    is_clicked = click_with_check(item)

            if not is_clicked:
                # Check if element is covered by another element
                overlay_xpath = f"//div[@style='pointer-events: none;']"
                overlays = self.browser.find_elements(By.XPATH, overlay_xpath)
                if overlays:
                    self.browser.execute_script("arguments[0].style.pointerEvents = 'none';", overlays[0])
                    sleep(1)
                    is_clicked = click_with_check(item)

            if not is_clicked:
                raise Exception(f"Element '{value}' could not be clicked.")

    def select_by_value_old2(self, locator, value):
        with allure.step('Select data in combobox by text'):
            try:
                combobox = self.find(locator)
                combobox.click()
                popup_xpath = (By.XPATH,
                               "//div[@class='dx-overlay-wrapper dx-popup-wrapper dx-dropdowneditor-overlay dx-dropdownlist-popup-wrapper dx-selectbox-popup-wrapper']")
                # Находим элемент popup с помощью указанного XPath
                popup_element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located(popup_xpath)
                )

                # Ищем элемент dx-scrollview-content внутри найденного popup
                scrollview_content = popup_element.find_element(By.XPATH, './/*[contains(@class, "dx-scrollview-content")]')

                # Находим все элементы dx-item dx-list-item внутри найденного элемента
                items = scrollview_content.find_elements(By.XPATH,
                                                         './/*[contains(@class, "dx-item") and contains(@class, "dx-item dx-list-item")]')

                # Ищем элемент с текстом
                for item in items:
                    if item.text.strip() == value:
                        print(f'Value {item.text.strip()} was found')
                        item.click()
                        return value

                combobox.click()

            except Exception as e:
                print(f"An error occurred: {e}")

            return None

    def select_by_value(self, locator, value):
        with allure.step('Select data in combobox by text'):
            try:
                combobox = self.find(locator)
                combobox.click()
                # sleep(0.5)

                popup_xpath = (By.XPATH,
                               "//div[@class='dx-overlay-wrapper dx-popup-wrapper dx-dropdowneditor-overlay dx-dropdownlist-popup-wrapper dx-selectbox-popup-wrapper']")
                # Находим элемент popup с помощью указанного XPath
                sleep(0.5)
                
                popup_element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located(popup_xpath)
                )

                # Ищем элемент dx-scrollview-content внутри найденного popup
                scrollview_content = WebDriverWait(popup_element, 10).until(
                    EC.visibility_of_element_located((By.XPATH, './/*[contains(@class, "dx-scrollview-content")]'))
                )

                # Находим все элементы dx-item dx-list-item внутри найденного элемента
                items = WebDriverWait(scrollview_content, 10).until(
                    EC.visibility_of_all_elements_located(
                        (By.XPATH, './/*[contains(@class, "dx-item") and contains(@class, "dx-list-item")]'))
                )

                # Ищем элемент с текстом и проверяем его кликабельность
                for item in items:
                    if item.text.strip() == value:
                        print(f'Value {item.text.strip()} was found')
                        allure.attach(self.browser.get_screenshot_as_png(), name='Select data in combobox',
                                      attachment_type=allure.attachment_type.PNG)
                        item.click()
                        return value
                combobox.click()

            except Exception as e:
                print(f"An error occurred: {e}")

            return None


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

    def validate(self, locator, value):
        try:
            # Найти ada-select-box по указанному локатору
            ada_select_box = self.browser.find_element(*locator)
            ada_select_box_id = ada_select_box.get_attribute('id')

            # Найти dx-select-box внутри ada-select-box
            dx_select_box = ada_select_box.find_element(By.XPATH, ".//dx-select-box")

            # нажать два раза
            dx_select_box.click()
            dx_select_box.click()

            # Найти все элементы с классом "dx-item dx-list-item" внутри dx-select-box
            items = dx_select_box.find_elements(By.XPATH, ".//div[contains(@class, 'dx-item dx-list-item')]")

            selected_item_text = None

            parent_id = ada_select_box_id
            for item in items:
                if item.get_attribute("aria-selected") == "true":
                    parent_element = item.find_element(By.XPATH, f"ancestor::ada-select-box[@id='{parent_id}']")
                    if parent_element:
                        selected_item_text = self.browser.execute_script("""
                                        var parent_id = arguments[0];
                                        var selectedItem = document.querySelector(`#${parent_id} div[aria-selected='true'] .dx-item-content.dx-list-item-content`);
                                        return selectedItem ? selectedItem.textContent.trim() : null;
                                    """, parent_id)  # Удаление лишних пробелов
                        break

            # Проверка, что значение selected_item_text равно ожидаемому значению value
            if selected_item_text == value:
                print(f"Selected value '{selected_item_text}' equal '{value}'")
                return selected_item_text
            else:
                print(f"Selected value '{selected_item_text}' was not equal '{value}'")
                return selected_item_text

        except NoSuchElementException as e:
            print(f"Элемент не найден или не удалось выполнить действие: {e}")
            return None




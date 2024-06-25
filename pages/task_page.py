from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from elements.combobox import ComboBox
import allure


task_name_field_locator = (By.XPATH, "//dx-text-box[@id='tbRecordName']//input")
task_status_field_locator = (By.XPATH, "//dx-text-box[@id='tbStatusName']//input")
task_vub_class_locator = (By.XPATH, "//dx-text-box[@id='tbVubClass']//input")
task_vub_sub_class_locator = (By.XPATH, "//dx-text-box[@id='tbVubSubClass']//input")
btn_expand_locator = (By.XPATH, "//div[@id='btnExpander']")
cmb_authority_locator = (By.XPATH, "//ada-select-box[@id='sbAuthority']")

temp = (By.XPATH, "//ada-select-box[@id='sbAuthority']")

temp2 = (By.XPATH, "//div[contains(@class, 'dx-item dx-list-item')]")


class TaskPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.cmb_priority_value = "Automatisch"

    def task_name_enter_text(self):
        return self.enter_text('test', task_name_field_locator)

    def task_name_value(self):
        return self.text_box_get_value(task_name_field_locator)

    def task_status_value(self):
        return self.text_box_get_value(task_status_field_locator)

    def button_expand_click(self):
        self.click(btn_expand_locator)

    def task_vub_class_value(self):
        return self.text_box_get_value(task_vub_class_locator)

    def task_vub_sub_class_value(self):
        return self.text_box_get_value(task_vub_sub_class_locator)

    def combobox_priority_click(self):
        return self.click(cmb_authority_locator)

    def combobox_count(self):
        return self.get_elements_values_by_xpath(temp)

    def get_elements_values(self):
        element = self.find(temp)
        items = element.find_elements(*temp2)
        return [item.text for item in items]

    def find_text_in_combobox(self, text):
        element = self.find(temp)
        items = element.find_elements(*temp2)
        matching_items = [item for item in items if item.text in text]
        return [item.text for item in matching_items]

    def priority_cmb_select_value(self, value):
        print(f'cmb has {ComboBox(self.browser).select_by_text(cmb_authority_locator, value)}')
        return ComboBox(self.browser).select_by_text(cmb_authority_locator, value)

    # def cmb_priority_validate_selected_item(self, value):
    #     cmb_value = self.priority_cmb_select_value(value)









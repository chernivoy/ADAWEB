from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


task_name_field_locator = (By.XPATH, "//dx-text-box[@id='tbRecordName']//input")
task_status_field_locator = (By.XPATH, "//dx-text-box[@id='tbStatusName']//input")
task_vub_class_locator = (By.XPATH, "//dx-text-box[@id='tbVubClass']//input")
task_vub_sub_class_locator = (By.XPATH, "//dx-text-box[@id='tbVubSubClass']//input")
btn_expand_locator = (By.XPATH, "//div[@id='btnExpander']")
cmb = (By.XPATH, "//ada-select-box[@id='sbAuthority']")

temp = (By.XPATH, "//ada-select-box[@id='sbAuthority']")

temp2 = (By.XPATH, "//div[contains(@class, 'dx-item dx-list-item')]")

class TaskPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

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
        return self.click(cmb)

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




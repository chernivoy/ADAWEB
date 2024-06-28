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
task_short_name_locator = (By.XPATH, "//dx-text-box[@id='tbShortName']//input")
task_number_locator = (By.XPATH, "//dx-text-box[@id='tbRecordNumber']//input")
task_remark_locator = (By.XPATH, "//dx-text-area[@id='taRemark']//textarea")
btn_expand_locator = (By.XPATH, "//div[@id='btnExpander']")
cmb_authority_locator = (By.XPATH, "//ada-select-box[@id='sbAuthority']")
cmb_priority_locator = (By.XPATH, "//ada-select-box[@id='sbPriority']")
cmb_significance_locator = (By.XPATH, "//ada-select-box[@id='sbSignificance']")


task_entry_user_name_locator = (By.XPATH, "//dx-text-box[@id='tbEntryUserName']//input")
task_executor_locator = (By.XPATH, "//dx-text-box[@id='tbExecuteUserName']//input")


cmb_dx_item = (By.XPATH, "//div[contains(@class, 'dx-item dx-list-item')]")


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

    @property
    def task_short_name(self):
        return self.text_box_get_value(task_short_name_locator)

    @property
    def task_number(self):
        return self.text_box_get_value(task_number_locator)

    @property
    def task_remark(self):
        return self.text_box_get_value(task_remark_locator)

    # authority
    def combobox_authority_click(self):
        return self.click(cmb_authority_locator)

    def combobox_authority_select_value(self, value):
        return ComboBox(self.browser).select_by_value(cmb_authority_locator, value)

    def combobox_authority_select_value_by_index(self, index):
        return ComboBox(self.browser).select_by_index(cmb_authority_locator, index)

    def combobox_authority_find_value_by_text(self, text):
        return ComboBox(self.browser).find_text(cmb_authority_locator, cmb_dx_item, text)

    def combobox_authority_validate(self, value):
        return ComboBox(self.browser).validate(cmb_authority_locator, value)

    # priority
    def combobox_priority_click(self):
        return self.click(cmb_priority_locator)

    def combobox_priority_select_value(self, value):
        return ComboBox(self.browser).select_by_value(cmb_priority_locator, value)

    def combobox_priority_select_value_by_index(self, index):
        return ComboBox(self.browser).select_by_index(cmb_priority_locator, index)

    def combobox_priority_find_value_by_text(self, text):
        return ComboBox(self.browser).find_text(cmb_priority_locator, cmb_dx_item, text)

    def combobox_priority_validate(self, value):
        return ComboBox(self.browser).validate(cmb_priority_locator, value)

    #significance
    def combobox_significance_click(self):
        return self.click(cmb_significance_locator)

    def combobox_significance_select_value(self, value):
        return ComboBox(self.browser).select_by_value(cmb_significance_locator, value)

    def combobox_significance_select_value_by_index(self, index):
        return ComboBox(self.browser).select_by_index(cmb_significance_locator, index)

    def combobox_significance_find_value_by_text(self, text):
        return ComboBox(self.browser).find_text(cmb_significance_locator, cmb_dx_item, text)

    def combobox_significance_validate(self, value):
        return ComboBox(self.browser).validate(cmb_significance_locator, value)

    def get_elements_values(self):
        element = self.find(cmb_authority_locator)
        items = element.find_elements(*cmb_dx_item)
        return [item.text for item in items]

    def task_entry_user_value(self):
        return self.text_box_get_value(task_entry_user_name_locator)

    def task_executor_value(self):
        return self.text_box_get_value(task_executor_locator)


















    # def cmb_priority_validate_selected_item(self, value):
    #     cmb_value = self.priority_cmb_select_value(value)









from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
from pages.my_tasks_page import MyTasksPage
from pages.task_page import TaskPage
from selenium import webdriver
from time import sleep
import allure

task_data = {
    'name': 'WEB TASK 0001',
    'status': 'Aufgabe angenommen',
    'class': 'Web_class',
    'sub_class': 'Web_sub_class',
    'authority': 'Bestätigung',
    'entry_user_name': 'Goldun, Anna',
    'executor': 'Goldun, Anna',
    'priority': 'sehr niedrig',
    'significance': 'hoch',
    'short_name': 'w_cw_s_c',
    'number': 'TAS0000372',
    'remark': 'Task for web app/ Dont touch please!'
}


@allure.feature('MyTasksPage')
@allure.story('Check find task on myTask page')
def test_my_tasks(login):
    # dashboard page
    dashboard_page = DashboardPage(login)
    dashboard_page.label_dashboard_click()
    sleep(1)
    dashboard_page.area_my_tasks_click()
    # my task page
    my_tasks_page = MyTasksPage(login)
    my_tasks_page.label_data_grid_locator_is_visible()
    my_tasks_page.search_field_enter_text(task_data['name'])
    my_tasks_page.label_data_grid_locator_is_visible()
    my_tasks_page.table_contains_text(task_data['name'])
    # task page
    task_page = TaskPage(login)
    task_page.button_expand_click()

    assert task_data['name'] == task_page.task_name_value(), "Name is not equal"
    assert task_data['status'] == task_page.task_status_value(), "Status is not equal"
    assert task_data['class'] == task_page.task_vub_class_value(), "Class is not equal"
    assert task_data['sub_class'] == task_page.task_vub_sub_class_value(), "Sub Class is not equal"
    assert task_data['entry_user_name'] == task_page.task_entry_user_value(), "User Name is not equal"
    assert task_data['executor'] == task_page.task_executor_value(), "Executor is not equal"
    assert task_data['short_name'] == task_page.task_short_name, "Short name is not equal"
    assert task_data['number'] == task_page.task_number, "Number is not equal"
    assert task_data['remark'] == task_page.task_remark, "Remark is not equal"
    assert task_data['authority'] == task_page.combobox_authority_validate(task_data['authority']), "Authority is not equal"
    assert task_data['priority'] == task_page.combobox_priority_validate(task_data['priority']), "Priority is not equal"
    assert task_data['significance'] == task_page.combobox_significance_validate(task_data['significance']), "Significance is not equal"





















    # task_page.combobox_priority_click()
    # sleep(1)
    # temp1 = task_page.get_elements_values()
    # print(f'count {temp1}')
    # findtext = task_page.find_text_in_combobox("Automatisch")
    # assert findtext == "Automatisch", 'Sub Class is not equal'
    # print(f'text  {findtext} is foound')

    sleep(1)


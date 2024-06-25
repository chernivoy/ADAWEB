from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
from pages.my_tasks_page import MyTasksPage
from pages.task_page import TaskPage
from selenium import webdriver
from time import sleep
import allure

task_name = 'WEB TASK 0001'
task_status = 'Aufgabe angenommen'
task_class = 'Web_class'
task_sub_class = 'Web_sub_class'


@allure.feature('MyTasksPage')
@allure.story('Check find task on myTask page')
def test_my_tasks(login):
    dashboard_page = DashboardPage(login)
    dashboard_page.label_dashboard_click()
    sleep(2)
    dashboard_page.area_my_tasks_click()
    # my task page
    my_tasks_page = MyTasksPage(login)
    my_tasks_page.label_data_grid_locator_is_visible()
    my_tasks_page.search_field_enter_text(task_name)
    my_tasks_page.label_data_grid_locator_is_visible()
    my_tasks_page.table_contains_text(task_name)
    # task page
    task_page = TaskPage(login)
    assert task_name == task_page.task_name_value(), "Name is not equal"
    assert task_status == task_page.task_status_value(), "Status is not equal Aufgabe angenommen"
    task_page.button_expand_click()
    assert task_class == task_page.task_vub_class_value(), "Class is not equal"
    assert task_sub_class == task_page.task_vub_sub_class_value(), 'Sub Class is not equal'

    task_page.priority_cmb_select_value(task_page.cmb_priority_value)

    sleep(5)


















    # task_page.combobox_priority_click()
    # sleep(1)
    # temp1 = task_page.get_elements_values()
    # print(f'count {temp1}')
    # findtext = task_page.find_text_in_combobox("Automatisch")
    # assert findtext == "Automatisch", 'Sub Class is not equal'
    # print(f'text  {findtext} is foound')

    sleep(1)


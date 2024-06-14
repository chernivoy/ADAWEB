from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
from pages.my_tasks_page import MyTasksPage
from selenium import webdriver
from time import sleep
import allure

task_name = 'WEB TASK 0001'


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
    sleep(1)


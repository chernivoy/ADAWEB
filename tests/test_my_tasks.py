from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
from pages.my_tasks_page import MyTasksPage
from selenium import webdriver
from time import sleep
import allure


@allure.feature('MyTasksPage')
@allure.story('Check count tasks on Dashboard page')
def test_my_tasks(login):
    dashboard_page = DashboardPage(login)
    dashboard_page.label_dashboard_click()
    sleep(5)
    dashboard_page.area_my_tasks_click()
    sleep(10)
    my_tasks_page = MyTasksPage(login)
    my_tasks_page.search_field_enter_value('Cyclic task 1')
    sleep(5)
    my_tasks_page.table_contains_text('Cyclic task 1')
    sleep(5)


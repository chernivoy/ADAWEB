from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
import pytest
from selenium import webdriver
from time import sleep
import allure


@allure.feature('Dashboard')
@allure.story('Check count tasks on Dashboard page')
def test_check_tasks_count_on_dashboard(login):
    dashboard_page = DashboardPage(login)
    dashboard_page.label_dashboard_is_displayed()
    dashboard_page.label_dashboard_click()
    dashboard_page.my_tasks_count()
    dashboard_page.given_tasks_count()
    dashboard_page.created_tasks_count()
    dashboard_page.watched_tasks_count()
    dashboard_page.favorite_tasks_count()
    sleep(2)
    dashboard_page.area_my_tasks_click()
    sleep(1)




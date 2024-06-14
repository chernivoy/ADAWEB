from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
import pytest
from selenium import webdriver
from time import sleep
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui



formulare_button_locator = (By.XPATH, "//*[contains(text(), 'Formulare')]")
# search_field_locator = (By.XPATH, "//input")
search_field_locator = (By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
search_field_locator2 = (By.XPATH, "/html/body/ubp-app-root/div/div/main/ubp-pdf-feature/ubp-common-layout-outlet/div/div/div/mat-form-field/div[1]/div[2]/div/input")
gas_kundennummer_locator = (By.XPATH, "//input[@name='gas_kundennummer']")
gas_verbraucherstellennummer_locator = (By.XPATH, "//input[@name='gas_verbraucherstellennummer']")
gas_vorname_locator = (By.XPATH, "//input[@name='gas_vorname']")


xpath = (
    "//a[@_ngcontent-ng-c1898213780='' and @mat-flat-button='' and @color='primary' "
    "and @mat-ripple-loader-class-name='mat-mdc-button-ripple' and contains(@class, 'mdc-button') "
    "and contains(@class, 'mdc-button--unelevated') and contains(@class, 'mat-mdc-unelevated-button') "
    "and contains(@class, 'mat-primary') and contains(@class, 'mat-mdc-button-base') and @href='/formulare']"
    "//span[@class='mdc-button__label' and text()='Formulare']"
)
@allure.feature('Dashboard')
@allure.story('Check count tasks on Dashboard page')
def test_document(browser_doc):
    url = 'http://192.168.102.120:8326/dashboard'
    browser_doc.get(url)
    sleep(1)
    browser_doc.find_element(By.XPATH, xpath).click()
    sleep(1)

    checkbox = WebDriverWait(browser_doc, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")))
    checkbox.click()
    sleep(1)

    buttons = WebDriverWait(browser_doc, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button")))

    # Нажмите на кнопку по индексу (например, на первую кнопку)
    buttons[1].click()
    sleep(5)

    gas_kundennummer = browser_doc.find_element(By.XPATH, "//input[@name='gas_kundennummer']")
    gas_kundennummer.send_keys('123456')
    gas_verbraucherstellennummer = browser_doc.find_element(By.XPATH, "//input[@name='gas_verbraucherstellennummer']")
    gas_verbraucherstellennummer.send_keys('789012')
    gas_vorname = browser_doc.find_element(By.XPATH, "//input[@name='gas_vorname']")
    gas_vorname.send_keys('Max')
    gas_name = browser_doc.find_element(By.XPATH, "//input[@name='gas_name']")
    gas_name.send_keys('Mustermann')
    gas_firmenname = browser_doc.find_element(By.XPATH, "//input[@name='gas_firmenname']")
    gas_firmenname.send_keys('Beispiel GmbH')
    gas_strasse = browser_doc.find_element(By.XPATH, "//input[@name='gas_strasse']")
    gas_strasse.send_keys('Musterstraße')
    gas_hausnummer = browser_doc.find_element(By.XPATH, "//input[@name='gas_hausnummer']")
    gas_hausnummer.send_keys('123')
    hsn_zusatz = browser_doc.find_element(By.XPATH, "//input[@name='hsn_zusatz']")
    hsn_zusatz.send_keys('A')
    gas_plz = browser_doc.find_element(By.XPATH, "//input[@name='gas_plz']")
    gas_plz.send_keys('10115')
    gas_ort = browser_doc.find_element(By.XPATH, "//input[@name='gas_ort']")
    gas_ort.send_keys('Berlin')
    gas_telefon = browser_doc.find_element(By.XPATH, "//input[@name='gas_telefon']")
    gas_telefon.send_keys('+49 30 12345678')
    gas_e_mail = browser_doc.find_element(By.XPATH, "//input[@name='gas_e_mail']")
    gas_e_mail.send_keys('maxx.mustermann@example.com')

    gas_abschlagshoehe_alt = browser_doc.find_element(By.XPATH, "//input[@name='gas_abschlagshoehe_alt']")
    gas_abschlagshoehe_alt.send_keys('50.00')

    gas_abschlagshoehe_neu = browser_doc.find_element(By.XPATH, "//input[@name='gas_abschlagshoehe_neu']")
    gas_abschlagshoehe_neu.send_keys('60.00')

    gas_datum_aenderung = browser_doc.find_element(By.XPATH, "//input[@name='gas_datum_aenderung']")
    gas_datum_aenderung.send_keys('01.07.2024')

    gas_ort_unterschrift = browser_doc.find_element(By.XPATH, "//input[@name='gas_ort_unterschrift']")
    gas_ort_unterschrift.send_keys('Berlin')

    gas_datum_unterschrift = browser_doc.find_element(By.XPATH, "//input[@name='gas_datum_unterschrift']")
    gas_datum_unterschrift.send_keys('15.06.2024')
    sleep(1)
    btn = browser_doc.find_element(By.XPATH, "//button[@class='mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-primary mat-mdc-button-base ng-star-inserted']")
    btn.click()
    sleep(1)

    sugnature = browser_doc.find_element(By.XPATH, "//canvas[@id='signatureCanvas-0']")
    sugnature.click()
    sleep(1)

    save_signature_button = browser_doc.find_element(By.XPATH, "//button[@class='mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-accent mat-mdc-button-base']")
    save_signature_button.click()
    sleep(1)

    btn_next = browser_doc.find_element(By.XPATH, "//button[@class='mat-stepper-next mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-primary mat-mdc-button-base ng-star-inserted']")
    btn_next.click()
    sleep(1)

    chksummary = browser_doc.find_element(By.XPATH, "//input[@id='matchck-request-summary-report-input']")
    chksummary.click()
    sleep(1)

    txt_email = browser_doc.find_element(By.XPATH, "//input[@id='ieml-user-email']")
    txt_email.click()
    txt_email.send_keys('chernivoy@gmail.com')
    sleep(1)

    txt_place_holder = browser_doc.find_element(By.XPATH, "//textarea[@placeholder='Ihren Kommentar hinzufügen']")
    txt_place_holder.click()
    txt_place_holder.send_keys('This message has been generated automatically.')
    sleep(3)

    # btn_attach = browser_doc.find_element(By.XPATH, "//button[@id='btn-files-attach']")
    # btn_attach.click()
    # sleep(3)

    btn_send = browser_doc.find_element(By.XPATH, "//button[@class='ml-auto mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-primary mat-mdc-button-base']")
    btn_send.click()
    sleep(3)

    # file_path = '/Users/macbook_igor/WEB/WEBADAICA/Folder1/test.txt'

    # # Используем PyAutoGUI для ввода пути к файлу и нажатия кнопки "Открыть"
    # pyautogui.write(file_path)
    # pyautogui.press('return')
    # time.sleep(10)  # Подождите, пока файл загрузится


    # WebDriverWait(browser_doc, timeout=10).until(EC.presence_of_element_located(search_field_locator))

    # search_input = browser_doc.find_element(search_field_locator)
    # search_input.click()
    # # sleep(5)
    # # search_input.send_keys("Änderungen der Abschlagshöhe Gas")
    # sleep(5)

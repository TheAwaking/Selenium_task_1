from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    url = 'https://store.steampowered.com/'
    chrome_browser.get(url)
    yield chrome_browser
    chrome_browser.quit()


class Locators:
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class,'global')]")
    TEXT = (By.XPATH, "//input[@type='text']")[1]
    PASS = (By.XPATH, "//input[@type='password']")
    SING_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_TEXT = (By.XPATH, "//div[contains(text(), 'Please check your password')]")


def test_site(driver):
    login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login.click()
    fake = Faker()
    name = fake.name()
    password = fake.password(length=12)
    account_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT))
    account_field.send_keys(name)
    password_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PASS))
    password_field.send_keys(password)
    sign_in = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SING_BUTTON))
    sign_in.click()
    login_error_alert = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))

    assert login_error_alert.is_displayed()



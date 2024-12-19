from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    url = 'https://store.steampowered.com/'
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class,'global')]")
    TEXT = (By.XPATH, "//input[@type='text']")
    PASS = (By.XPATH, "//input[@type='password']")
    SING_BUTTON = (By.XPATH, "//button[@type='submit']")
    CHECK = (By.XPATH, "//*[@type='password']")
    ERROR_TEXT = (By.XPATH, "//button[@type='submit']/following::div [@class]")
    ALERT_TEXT = (By.XPATH, "//div[contains(text(), 'Please check your password')]")
    TIMEOUT = 10


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.get(Locators.url)
    yield chrome_browser
    chrome_browser.quit()


def test_site(driver):
    wait = WebDriverWait(driver, Locators.TIMEOUT)
    login = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login.click()
    fake = Faker()
    name = fake.name()
    password = fake.password(length=12)
    wait.until(EC.presence_of_element_located(Locators.CHECK))
    account_field = wait.until(EC.visibility_of_element_located(Locators.TEXT))
    account_field.send_keys(name)
    password_field = wait.until(EC.visibility_of_element_located(Locators.PASS))
    password_field.send_keys(password)
    sign_in = wait.until(EC.element_to_be_clickable(Locators.SING_BUTTON))
    sign_in.click()
    wait.until(
        EC.visibility_of_element_located(Locators.ERROR_TEXT))

    assert wait.until(
        EC.visibility_of_element_located(Locators.ALERT_TEXT)).is_displayed()

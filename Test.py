from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    chrome_browser.maximize_window()
    return chrome_browser


def test_site(driver):
    driver.get('https://store.steampowered.com/')
    driver.find_element(By.XPATH, "//a[contains(@class,'global')]").click()
    fake = Faker()
    name = fake.name()
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(name)
    password = fake.password(length=12)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@class='DjSvCZoKKfoNSmarsEcTS']").click()
    wait = WebDriverWait(driver, 5)
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'_1W_6HXiG4JJ0By1qN_0fGZ')]")))

    assert element.is_displayed()

    # изменение

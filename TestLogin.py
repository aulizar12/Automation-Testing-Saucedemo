import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class Prerequest:
    username = 'standard_user'
    password = 'secret_sauce'


@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()


def test_login_valid(setup):
    setup.find_element(By.NAME, 'user-name').send_keys(Prerequest.username)
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys(Prerequest.password)
    time.sleep(1)
    setup.find_element(By.ID, 'login-button').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    setup.find_element(By.ID, 'logout_sidebar_link').click()
    time.sleep(2)


def test_login_invalid_username(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("ciko")
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys(Prerequest.password)
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username and password do not match any user in this service" == response_message)


def test_login_invalid_username_empty(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("")
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys(Prerequest.password)
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username is required" == response_message)


def test_login_invalid_password(setup):
    setup.find_element(By.NAME, 'user-name').send_keys(Prerequest.username)
    time.sleep(3)
    setup.find_element(By.NAME, 'password').send_keys("ciko")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username and password do not match any user in this service" == response_message)


def test_login_invalid_password_empty(setup):
    setup.find_element(By.NAME, 'user-name').send_keys(Prerequest.username)
    time.sleep(3)
    setup.find_element(By.NAME, 'password').send_keys("")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Password is required" == response_message)


def test_login_invalid(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("haciko")
    time.sleep(3)
    setup.find_element(By.NAME, 'password').send_keys("ciko08")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username and password do not match any user in this service" == response_message)

def test_login_AllEmpty(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("")
    time.sleep(3)
    setup.find_element(By.NAME, 'password').send_keys("")
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username is required" == response_message)
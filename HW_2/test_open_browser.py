from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    about_link.click()
    sleep(2)
    driver.save_screenshot("test_about_page.png")
    sleep(2)


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.ID, "my-iframe"))))

    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p:nth-child(2)')))

    assert "semper posuere integer et senectus justo curabitur." in element.text




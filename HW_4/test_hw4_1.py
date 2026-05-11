import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://uitestingplayground.com/textinput"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    # Находим поле ввода
    input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#newButtonName")))

    # Вводим текст
    input_field.clear()
    input_field.send_keys("ITCH")

    # Находим кнопку
    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()

    # Проверяем изменение текста кнопки
    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH"))
    print(f"Текст кнопки: {button.text}")
    assert button.text == "ITCH"

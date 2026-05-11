import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_loading_images(driver):
    wait = WebDriverWait(driver, 20)
    driver.get(BASE_URL)

    # Ждём появления всех изображений
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4)
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))

    # Берём третье изображение
    third_image = images[2]

    # Получаем alt
    alt_value = third_image.get_attribute("alt")
    print(f"Alt третьего изображения: {alt_value}")

    # Проверка
    assert alt_value == "award"
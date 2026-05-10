from time import sleep
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "https://itcareerhub.de/ru"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_itcareerhub(driver):
    wait = WebDriverWait(driver, 10)

    # Открытие сайта
    driver.get(BASE_URL)

    # Проверка логотипа
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[alt="IT Career Hub"]')))

    assert logo.is_displayed()

    # Проверка пунктов меню

    expected_links = [
        "Программы",
        "Способы оплаты",
        "О нас",
        "Bildungsgutschein",
        "Отзывы",
        "Блог"
    ]

    for text in expected_links:
        element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
        assert element.is_displayed()
    # Проверка пункта "Контакты" в подменю "О нас"
    about_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "О нас")))

    actions = ActionChains(driver)
    actions.move_to_element(about_button).perform()

    contacts_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Контакты")))

    assert contacts_button.is_displayed()


    # Переключение языка RU -> DE

    button_de = driver.find_element(By.CSS_SELECTOR, '.tn-elem__19217104631710153064158 a')
    button_de.click()

    time.sleep(2)

    assert driver.current_url == "https://itcareerhub.de/"
    assert "itcareerhub.de/" in driver.current_url

    heading_de = driver.find_element(By.TAG_NAME, 'h1')
    expected_part = "Erwerben Sie einen gefragten IT-Beruf und starten Sie Ihre Karriere in Deutschland"
    assert expected_part in heading_de.text

    time.sleep(2)

    # Переключение языка DE -> RU

    button_ru = driver.find_element(By.CSS_SELECTOR, 'div[data-elem-id="176037137750141060"] a')
    button_ru.click()

    time.sleep(2)


    assert "itcareerhub.de/ru" in driver.current_url
    assert "/ru" in driver.current_url

    heading_final = driver.find_element(By.TAG_NAME, 'h1')
    assert "Начните IT карьеру" in heading_final.text


    # Клик по разделу "Контакты"
    about_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "О нас")))
    actions = ActionChains(driver)
    actions.move_to_element(about_button).perform()
    contacts_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Контакты")))

    assert contacts_button.is_displayed()
    contacts = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Контакты")))
    contacts.click()
    wait.until(lambda d: "contact" in d.current_url)
    time.sleep(2)


    # Клик по кнопке "Обратный звонок"
    callback = driver.find_element(By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")
    driver.execute_script( "arguments[0].scrollIntoView({block: 'center'});",callback)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")))
    driver.execute_script("arguments[0].click();", callback)
    time.sleep(2)

    # Проверка текста popup окна
    popup_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
    assert "Запишитесь на бесплатную карьерную консультацию" in popup_text.text

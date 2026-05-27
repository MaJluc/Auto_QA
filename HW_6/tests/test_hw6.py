from HW_6.pages.checkout_total_page import CheckoutTotalPage
from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.login_page import LoginPage
from HW_6.pages.card_page import CardPage
from HW_6.pages.checkout_info_page import CheckoutInfoPage


def test_checkout_total(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    card_page = CardPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_total_page = CheckoutTotalPage(driver)

    login_page.open_page(driver)
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart()
    inventory_page.open_cart()
    card_page.checkout()
    checkout_info_page.checkout_info("Maxx", "Bugger", "12345")
    checkout_info_page.click_continue()
    total_price = checkout_total_page.get_total_price()
    assert total_price == 58.29
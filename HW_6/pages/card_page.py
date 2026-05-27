from selenium.webdriver.common.by import By

from HW_6.pages.base_page import BasePage


class CardPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")


    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
from .base_page import BasePage
from .locators import MvdPageLocators

class MvdPage(BasePage):
    def back_to_catalog(self):
        text2 = self.driver.find_element(*MvdPageLocators.PRODUCT_PRICE_ON_PAGE)

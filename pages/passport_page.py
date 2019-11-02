from .base_page import BasePage
from .locators import PassportPageLocators

class PassportPage(BasePage):
    def back_to_catalog(self):
        back_button = self.driver.find_element(*PAssportPageLocators.BACK_BUTTON)
        back_to_catalog_button = self.driver.find_element(*PAssportPageLocators.BACK_TO_CATALOG_BUTTON)
        back_button.click()
        back_button.click()
        back_to_catalog_button.click()

from .base_page import BasePage
from .locators import PassportPageLocators

class PassportPage(BasePage):
    def in_the_catalog(self):
        back_button = self.driver.find_element(*PassportPageLocators.BACK_BUTTON)
        back_button.click()
        back_button_2 = self.driver.find_element(*PassportPageLocators.BACK_BUTTON_2)
        back_button_2.click()
        back_to_catalog_button = self.driver.find_element(*PassportPageLocators.BACK_TO_CATALOG_BUTTON)
        back_to_catalog_button.click()

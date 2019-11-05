from .base_page import BasePage
from .locators import MvdPageLocators

class MvdPage(BasePage):
    def open_and_go_to_documents(self):
        menu_button = self.driver.find_element(*MvdPageLocators.MVD_MENU_BUTTON)
        menu_button.click()
        documents_button = self.driver.find_element(*MvdPageLocators.MVD_MENU_DOCUMENTS_BUTTON)
        documents_button.click()

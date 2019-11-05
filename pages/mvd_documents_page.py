from .base_page import BasePage
from .locators import MvdDocumentsPageLocators

class MvdDocumentsPage(BasePage):
    def open_and_go_to_documents(self):
        another_documents = self.driver.find_element(*MvdDocumentsPageLocators.MVD_DOCUMENTS_PAGE_ANOTHER_DOCUMENTS)
        another_documents.click()

    def download_document(self):
        documents_button = self.driver.find_element(*MvdDocumentsPageLocators.MVD_ANOTHER_DOCUMENTS_PAGE_RANDOM_DOCUMENT)
        documents_button.click()

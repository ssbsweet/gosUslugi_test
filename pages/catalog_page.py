from .base_page import BasePage
from .locators import CatalogPageLocators

class CatalogPage(BasePage):
    def back_to_catalog(self):
        text2 = self.driver.find_element(*CatalogPageLocators.CATALOG_PAGE_NAME)
        text1 = "Каталог госуслуг"
        assert text2.text == text1
        print('User on catalog page')

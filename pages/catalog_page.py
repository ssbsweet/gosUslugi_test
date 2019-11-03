from .base_page import BasePage
from .locators import CatalogPageLocators

class CatalogPage(BasePage):
    def back_to_catalog(self):
        text2 = self.driver.find_element(*CatalogPageLocators.PRODUCT_PRICE_ON_PAGE)
        text1 = "Каталог госуслуг"
        assert text2.text == text1
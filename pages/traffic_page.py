import time

from .base_page import BasePage
from .locators import TrafficPageLocators

class TrafficPage(BasePage):
    def go_to_mvd_rossii(self):
        go_to_mvd_rossii_site = self.driver.find_element(*TrafficPageLocators.GO_TO_MVD_ROSSII_SITE)
        go_to_mvd_rossii_site.click()

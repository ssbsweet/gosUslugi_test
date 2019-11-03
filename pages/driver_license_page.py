from .base_page import BasePage
from .locators import DriverLicensePageLocators

class DriverLicensePage(BasePage):
    def go_to_website_of_the_traffic(self):
        website_of_the_traffic = self.driver.find_element(*DriverLicensePageLocators.WEBSITE_OF_THE_TRAFFIC)
        website_of_the_traffic.click()
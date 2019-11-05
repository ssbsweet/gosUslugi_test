import time

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SearchFormLoactors


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def fill_the_search_field(self):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FORM_INPUT_FIELD)
        search_field.click()
        time.sleep(1)
        search_field.send_keys('загран')
        new_generation_of_18_years = self.driver.find_element(*SearchFormLoactors.PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS)
        new_generation_of_18_years.click()
        time.sleep(2)




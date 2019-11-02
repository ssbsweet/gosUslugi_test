from .base_page import BasePage
from .locators import SearchPageLocators

class SearchPage(BasePage):
    def should_be_passport_of_a_new_generation_of_18_years(self):
        assert self.is_element_present(*SearchPageLocators.PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS), '' \
                                                        'PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS is not presented,'\
                                                        'probably wrong search result'

    def go_to_getting_a_passport_page(self):
        passport_of_a_new_generation_of_18_years = self.drive.find_element(*SearchPageLocators.PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS)
        passport_of_a_new_generation_of_18_years.click()
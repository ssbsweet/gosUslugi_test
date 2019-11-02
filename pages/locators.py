from selenium.webdriver.common.by import By

class BasePageLocators:
    SITE_LOGO = (By.CSS_SELECTOR, ".logo")
    USER_TYPE_PICKER = (By.CSS_SELECTOR, "#mainCiviPicker")
    USER_LOCATION_PICKER = (By.CSS_SELECTOR, "#locationButton")
    USER_LANGUAGE_PICKER = (By.CSS_SELECTOR, "#langCiviPicker")

class MainPageLocators:
    SEARCH_FORM_INPUT_FIELD = (By.CSS_SELECTOR, "#_epgu_el1")
    SEARCH_FORM_BUTTON = (By.CSS_SELECTOR, ".btn-base.medium.search")

class SearchFormLoactors:
    PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS = (By.CSS_SELECTOR, ".dropdown-el__li:nth-child(3)")

class SearchPageLocators:
    PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS = (By.CSS_SELECTOR, "div:nth-child(3) > div > span > a")

class PassportPageLocators:
    BACK_BUTTON = (By.CSS_SELECTOR, ".btn-sec.larr_svg.ng-scope.small")
    BACK_TO_CATALOG_BUTTON = (By.CSS_SELECTOR, ".btn-sec.small.larr")
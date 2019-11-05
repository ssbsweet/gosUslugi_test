from selenium.webdriver.common.by import By

class BasePageLocators:
    SITE_LOGO = (By.CSS_SELECTOR, ".logo")
    USER_TYPE_PICKER = (By.CSS_SELECTOR, "#mainCiviPicker")
    USER_LOCATION_PICKER = (By.CSS_SELECTOR, "#locationButton")
    USER_LANGUAGE_PICKER = (By.CSS_SELECTOR, "#langCiviPicker")

class MainPageLocators:
    SEARCH_FORM_INPUT_FIELD = (By.CSS_SELECTOR, ".searchBox--main input")
    SEARCH_FORM_BUTTON = (By.CSS_SELECTOR, ".btn-base.medium.search")

class SearchFormLoactors:
    PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS = (By.CSS_SELECTOR, ".dropdown-el__li:nth-child(3)")

class SearchPageLocators:
    PASSPORT_OF_A_NEW_GENERATION_OF_18_YEARS = (By.CSS_SELECTOR, "#content > div.ng-scope > div > div.result_search.limiter.ng-scope > div.details > div:nth-child(3) > div > span > a")

class PassportPageLocators:
    BACK_BUTTON = (By.CSS_SELECTOR, ".btn-sec.larr_svg.ng-scope.small")
    BACK_BUTTON_2 = (By.CSS_SELECTOR, ".btn-sec.small.larr_svg")
    BACK_TO_CATALOG_BUTTON = (By.CSS_SELECTOR, ".btn-sec.small.larr")

class CatalogPageLocators:
    CATALOG_PAGE_NAME = (By.CSS_SELECTOR, ".h1.offset-top-none.offset-bottom-md.light.ng-binding.ng-scope")

class DriverLicensePageLocators:
    WEBSITE_OF_THE_TRAFFIC = (By.CSS_SELECTOR, "#printableArea > div:nth-child(3) > div:nth-child(1) > div > div > div.span_14 > div > div:nth-child(1) > p:nth-child(1) > a")

class TrafficPageLocators:
    GO_TO_MVD_ROSSII_SITE = (By.CSS_SELECTOR, "body > div.ln-page > div > div:nth-child(11) > div.bs-holder2 > ul > li:nth-child(3) > a")

class MvdPageLocators:
    MVD_MENU_BUTTON = (By.CSS_SELECTOR, "#menu-1 > li:nth-child(1) > a")
    MVD_MENU_DOCUMENTS_BUTTON = (By.CSS_SELECTOR, ".active li:nth-child(9) > a")

class MvdDocumentsPageLocators:
    MVD_DOCUMENTS_PAGE_ANOTHER_DOCUMENTS = (By.CSS_SELECTOR, ".ul-sub-list > li:nth-child(11) > a")
    MVD_ANOTHER_DOCUMENTS_PAGE_RANDOM_DOCUMENT = (By.CSS_SELECTOR, "tr:nth-child(1) .file_a")


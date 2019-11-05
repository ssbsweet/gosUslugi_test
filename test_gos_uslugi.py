import time

import pytest

from .pages.catalog_page import CatalogPage
from .pages.driver_license_page import DriverLicensePage
from .pages.main_page import MainPage
from .pages.mvd_documents_page import MvdDocumentsPage
from .pages.mvd_page import MvdPage
from .pages.passport_page import PassportPage
from .pages.search_page import SearchPage
from .pages.traffic_page import TrafficPage

@pytest.mark.need_review
def test_all_test_work_1(driver):
    link = "https://www.gosuslugi.ru/"
    mainPage = MainPage(driver, link)
    mainPage.open()
    driver.maximize_window()
    time.sleep(2)
    mainPage.fill_the_search_field()
    searchPage = SearchPage(driver, link)
    searchPage.should_be_passport_of_a_new_generation_of_18_years()
    searchPage.go_to_getting_a_passport_page()
    passportPage = PassportPage(driver, link)
    passportPage.in_the_catalog()
    catalogPage = CatalogPage(driver, link)
    catalogPage.back_to_catalog()

@pytest.mark.need_review
def test_all_test_work_2(driver):
    link = "https://www.gosuslugi.ru/situation/obtaining_drivers_license_first_time"
    driverLicensePage = DriverLicensePage(driver, link)
    driverLicensePage.open()
    driver.maximize_window()
    driverLicensePage.go_to_website_of_the_traffic()
    time.sleep(5)
    trafficPage = TrafficPage(driver, link)
    trafficPage.close_last_tab()
    trafficPage.go_to_mvd_rossii()
    mvdRossiiPage = MvdPage(driver, link)
    mvdRossiiPage.close_last_tab()
    mvdRossiiPage.open_and_go_to_documents()
    mvdDocuments = MvdDocumentsPage(driver, link)
    mvdDocuments.open_and_go_to_documents()
    mvdDocuments.download_document()
    mvdDocuments.is_file_exist()
    time.sleep(2)
    mvdDocuments.remove_file()
    time.sleep(2)




import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url

    def go_to_main_page(self):
        link = self.driver.find_element(*BasePageLocators.SITE_LOGO)
        link.click()

    def go_to_getting_a_driver_license_first_time_page(self):
        link = "https://www.gosuslugi.ru/situation/obtaining_drivers_license_first_time"
        link.open()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        print(type(self.driver))
        self.driver.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User icon is not presented,' \
                                                                     ' probably unauthorised user'
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def close_last_tab(self):
        if (len(self.driver.window_handles) == 2):
            self.driver.switch_to.window(driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(driver.window_handles[0])

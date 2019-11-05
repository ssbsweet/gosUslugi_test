import os
import os.path

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators

class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def go_to_main_page(self):
        link = self.driver.find_element(*BasePageLocators.SITE_LOGO)
        link.click()

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

    def close_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def scroll_down_method(self):
        self.driver.execute_script("window.scrollTo(0,2080)")

    def is_file_exist(self):
        PATH = './Downloads/0001201901220003.pdf'
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print("File exists and is readable")
        else:
            print("Either the file is missing or not readable")

    def remove_file(self):
        PATH = './Downloads/0001201901220003.pdf'
        if os.path.isfile(PATH):
            os.remove(PATH)
        else:  ## Show an error ##
            print("Error: %s file not found" % PATH)


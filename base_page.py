from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

class BasePage:
    """
    A Base class for TestPage.
    """
    def __init__(self, driver):
        """
        Initialize constructor, initializes WebDriver and defines 
        path to a testing page which located in root of program
        """
        self.driver = driver
        self.source_page = "file:///" + os.getcwd() + "//qa-test.html"

    def find_element(self, locator):
        """
        Returns element by its locator
        """
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator),
                                                      message=f"{locator}")

    def go_to_source_page(self):
        """
        Returns page to initial state
        """
        return self.driver.get(self.source_page)
from typing import Any

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTools:
    """Commonly required parts for testing"""

    def __init__(self, driver: Any) -> None:
        self.driver = driver
        self.timeout = 20

    def find_elements(self, locator: Any) -> Any:
        """
        return elements on a page
        """
        driver = self.driver
        try:
            element = driver.find_elements(*locator)
            return element
        except NoSuchElementException:
            return None

    def find_element_with_wait(self, locator: Any) -> Any:
        """
        return element when present on a page
        """
        web_driver_wait = WebDriverWait(self.driver, self.timeout)

        try:
            located = EC.presence_of_element_located(locator)
            element = web_driver_wait.until(located)
            return element
        except NoSuchElementException:
            return None

    def is_clickable_element(self, locator: Any) -> Any:
        """
        return element when present on  a page
        """
        web_driver_wait = WebDriverWait(self.driver, self.timeout)
        try:
            clickable = EC.element_to_be_clickable(locator)
            element = web_driver_wait.until(clickable)
            return element
        except TimeoutException:
            return None

    def does_element_exist(self, locator: Any) -> bool:
        """
        return element on the DOM of a page
        """
        driver = self.driver
        try:
            driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CLICK_RETRY_COUNT = 3


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def find(self, locator) -> WebElement:
        return self.wait().until(EC.presence_of_element_located(locator))

    def find_many(self, locator) -> list:
        return self.wait().until(EC.presence_of_all_elements_located(locator))

    def wait(self, timeout=30):
        """ Явное ожидание """
        return WebDriverWait(self.driver, timeout)

    def click(self, locator, timeout=30):
        """ Клик по элементу locator """
        for i in range(CLICK_RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < CLICK_RETRY_COUNT - 1:
                    pass
                else:
                    raise

    def send_keys(self, locator, keys):
        field = self.find(locator)
        field.clear()
        field.send_keys(keys)

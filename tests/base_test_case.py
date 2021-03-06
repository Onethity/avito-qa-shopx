import pytest

from ui.pages.main_page import MainPage


class BaseTestCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.main_page: MainPage = MainPage(driver)

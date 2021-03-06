from ui.locators.locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.catalog_page import CatalogPage


class MainPage(BasePage):
    """ Главная страница """
    locators = MainPageLocators()

    def auth(self, login, password):
        """ Авторизация """
        self.click(self.locators.OPEN_AUTH_LINK)
        self.send_keys(self.locators.LOGIN_INPUT, login)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.AUTH_BUTTON)

    def go_to_catalog(self):
        """ Переход к списку объявлений из категории 'Личные вещи' """
        self.click(self.locators.MORE_CATEGORIES_BUTTON)
        self.click(self.locators.PERSONAL_CATALOG_BUTTON)

        return CatalogPage(self.driver)

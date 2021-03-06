import random

from ui.locators.locators import CatalogPageLocators
from ui.pages.advert_page import AdvertPage
from ui.pages.base_page import BasePage


class CatalogPage(BasePage):
    """ Страница списка объявлений """
    locators = CatalogPageLocators()

    def apply_delivery_filter(self):
        """ Применить фильтр 'С Авито Доставкой' """
        self.click(self.locators.ONLY_DELIVERY_CHECKBOX)
        self.click(self.locators.SUBMIT_FILTER_BUTTON)

    def go_to_random_advert(self):
        """ Перейти к случайному объявлению """
        advert_links = self.find_many(self.locators.ADVERT_LINKS)
        random.choice(advert_links).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Переход на новую вкладку
        return AdvertPage(self.driver)

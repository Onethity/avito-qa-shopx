from ui.locators.locators import AdvertPageLocators
from ui.pages.base_page import BasePage
from ui.pages.delivery_page import DeliveryPage


class AdvertPage(BasePage):
    """ Страница объявления """
    locators = AdvertPageLocators()

    def go_to_delivery(self):
        """ Переход к доставке """
        self.click(self.locators.BUY_WITH_DELIVERY_BUTTON)
        return DeliveryPage(self.driver)

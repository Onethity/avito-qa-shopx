from ui.locators.locators import DeliveryPageLocators
from ui.pages.base_page import BasePage


class DeliveryPage(BasePage):
    """ Страница оформления доставки"""
    locators = DeliveryPageLocators()

    def get_phone_input_value(self):
        """ Получение значения поля 'Телефон' """
        field = self.find(self.locators.PHONE_INPUT)
        return field.get_attribute('value')

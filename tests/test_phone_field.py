import time

from tests.base_test_case import BaseTestCase


class TestPhoneField(BaseTestCase):
    def test_is_phone_empty(self, auth):
        """
         Проверяем, что при оформлении доставки поле "телефон" - пустое. Шаги:

         1. Открываем главную страницу и нажимаем "Вход и регистрация"
         2. Вводим логин в поле "Телефон или электронная почта"
         3. Вводим пароль в поле "Пароль"
         4. Нажимаем кнопку "Войти"
         5. В главном меню (справа от логотипа) нажимаем "ещё..."
         6. В открывшемся списке категорий выбираем "Личные вещи"
         7. Слева в фильтре нажимаем чекбокс "С Авито Доставкой"
         8. Нажимаем кнопку "Показать ... объявлений"
         9. Кликаем на заголовок случайного объявления
         10. Нажимаем на кнопку "Купить с доставкой"
         11. Проверяем value у поля "Телефон"

         Ожидаемое поведение: поле "Телефон" пустое (value=="")
        """
        catalog = self.main_page.go_to_catalog()
        catalog.apply_delivery_filter()

        advert = catalog.go_to_random_advert()
        delivery = advert.go_to_delivery()

        assert delivery.get_phone_input_value() == ''

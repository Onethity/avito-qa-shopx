from selenium.webdriver.common.by import By


class MainPageLocators:
    """ Локаторы главной страницы """
    OPEN_AUTH_LINK = (By.XPATH, '//a[@href="#login?authsrc=h"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="login"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    AUTH_BUTTON = (By.XPATH, '//div[contains(@class, "auth-form")]/button')

    MORE_CATEGORIES_BUTTON = (By.XPATH, '//a[@data-marker="more-link"]')
    PERSONAL_CATALOG_BUTTON = (By.XPATH, '//div[contains(@class, "top-rubricator-column")]//a[text()="Личные вещи"]')


class CatalogPageLocators:
    """ Локаторы страницы с объявлениями """
    ONLY_DELIVERY_CHECKBOX = (By.XPATH, '//label[@data-marker="delivery-filter"]')
    SUBMIT_FILTER_BUTTON = (By.XPATH, '//button[@data-marker="search-filters/submit-button"]')
    ADVERT_LINKS = (By.XPATH, '//a[@data-marker="item-title"]')


class AdvertPageLocators:
    """ Локаторы страницы объявления """
    BUY_WITH_DELIVERY_BUTTON = (By.XPATH, '//button[@data-marker="courier-item-button-main"]')


class DeliveryPageLocators:
    """ Локаторы страницы оформления доставки """
    PHONE_INPUT = (By.NAME, 'phone')

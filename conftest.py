import json
import time

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from config import CONFIG
from ui.pages.main_page import MainPage


def pytest_addoption(parser: Parser):
    """ Параметры запуска тестов """
    parser.addoption('--browser', default='chromium')
    parser.addoption('--selenoid', default=None)


class UnsupportedBrowserException(Exception):
    """ Исключение для неподдерживаемого браузера """
    pass


@pytest.fixture(scope='function')
def driver(config, request: FixtureRequest):
    """ Фикстура драйвера selenium """
    browser = request.config.getoption('--browser')
    selenoid = request.config.getoption('--selenoid')

    if selenoid:
        # Запуск тестов на selenoid
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "89.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://{}/wd/hub".format(selenoid),
            desired_capabilities=capabilities)
    else:
        # Запуск тестов локально
        # Устанавливаем драйвер для нужного браузера через webdriver_manager
        if browser == 'chrome':
            manager = ChromeDriverManager()
            driver = webdriver.Chrome(manager.install())
        elif browser == 'chromium':
            manager = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM)
            driver = webdriver.Chrome(manager.install())
        elif browser == 'firefox':
            manager = GeckoDriverManager()
            driver = webdriver.Firefox(executable_path=manager.install())
        else:
            raise UnsupportedBrowserException(
                f'Unsupported browser "{browser}". You must type one of "chrome", "chromium" or "firefox"')

    driver.maximize_window()
    driver.get(config['app_full_url'])

    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def config():
    """ Фикстура, содержащая конфигурацию тестов """
    return CONFIG


@pytest.fixture(scope='function')
def auth(driver, config):
    """ Фикстура для авторизации """
    MainPage(driver).auth(config['login'], config['password'])

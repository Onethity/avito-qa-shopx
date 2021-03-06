# ShopX-QA-trainee
## Тестовое задание

Полное описание задания находится [тут](https://github.com/avito-tech/ShopX-QA-trainee/blob/main/README.md).

### Задача 1
Решение в файле [TaskTestData.md](TaskTestData.md)


### Задача 2
Автотест написан на Python 3.8 c использованием паттерна PageObject.

Порядок запуска:
* Склонировать репозиторий:
`git clone https://github.com/Onethity/avito-qa-shopx.git`

* Установить зависимости: `pip install -r requirements.txt`

* Настроить конфигурацию тестов в файле [config.py](config.py)

* Запуск теста:
`pytest -s -l -v --browser=<browser>`

`<browser>` - название браузера для проведения тестирования. Можно выбрать `chrome` или `chromium`. Автотест будет запущен локально, нужный драйвер установится автоматически с помощью webdriver_manager. Если браузер не задан, то тесты запускаются в Chromium.

Если запустить тесты с ключом `--selenoid <selenoid_adress>`, например, `--selenoid localhost:4444`, тогда автотест будет исполняться удаленно на Selenoid.

# Проект по тестированию сервиса электронных и аудиокниг "Литрес"

> [Ссылка на сайт](https://www.litres.ru)

![This is an image](media/images/litres_main_page.png)

### Список проверок, реализованных в автотестах:

### UI-тесты
- [x] Авторизация пользователя(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Удаление книги из корзины
- [x] Выход из аккаунта

----
### Проект реализован с использованием:
<img src="media/icons/python-original.svg" width="50"> <img src="media/icons/pytest.png" width="50"> <img src="media/icons/selene.png" width="50"> <img src="media/icons/selenoid.png" width="50"> <img src="media/icons/jenkins.png" width="50"> <img src="media/icons/allure_report.png" width="50"> <img src="media/icons/allure_testops.png" width="50"> <img src="media/icons/jira.png" width="50"> <img src="media/icons/tg.png" width="50">

- Язык: `Python`
- Для написания UI-тестов используется фреймворк `Selene`, "обёртка" вокруг `Selenium WebDriver`
- Библиотека модульного тестирования: `PyTest`
- `Jenkins` выполняет удаленный запуск тестов.
- `Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)
- Фреймворк`Allure Report` собирает графический отчет о прохождении тестов
- После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант отчёта
- Полная статистика по прохождению тестов хранится в `Allure TestOps`
- Настроена интеграция `Allure TestOps` с `Jira`

----
### Локальный запуск
> Перед запуском в корне проекта создать файл .env с содержимым:
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud

EMAIL={email of your test litres account}
PASSWORD={password of your test litres account}

UNREGISTERED_EMAIL={any unregistered email on litres}
WRONG_PASSWORD=wrongpassword
```

> Для локального запуска необходимо выполнить (ключ выбора версии --browser-version не обязателен):
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s . --browser_version=128.0
```

----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> [Ссылка на проект в Jenkins](https://jenkins.autotests.cloud/job/litres_autotest_project/)

#### Параметры сборки

- `BROWSER_VERSION` - версия браузера (браузер `Chrome`)
- `COMMENT` - комментарий


#### Для запуска автотестов в Jenkins

1. Открыть [проект](https://jenkins.autotests.cloud/job/litres_autotest_project/)
2. Выбрать пункт `Build with Parameters`
3. Указать версию браузера
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure отчет


#### Общие результаты
![This is an image](media/images/allure_report_overview.png)
#### Список тест кейсов и пример отчета о прохождении теста
![This is an image](media/images/allure_report_behaviors.png)

----
### Полная статистика хранится в Allure TestOps
> [Ссылка на проект в AllureTestOps](https://allure.autotests.cloud/project/4670/dashboards)

#### Дашборд с общими показателями тестовых прогонов

![This is an image](media/images/allure_testops_dashboards.png)

#### История запуска тестовых наборов

![This is an image](media/images/allure_testops_launches.png)

#### Тест кейсы

![This is an image](media/images/allure_testops_test_cases.png)

#### Тестовые артефакты

![This is an image](media/images/allure_testops_attachments.png)

----

### Интеграция с Jira

> [Ссылка на проект в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1421)

![This is an image](media/images/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
> [Ссылка на канал в Telegram](https://t.me/litres_autotest)

![This is an image](media/images/telegram_report.png)

----
### Пример видео прохождения ui-автотеста
![autotest_gif](media/images/autotest.gif)

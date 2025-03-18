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
### Удаленный запуск автотестов выполняется на сервере Jenkins
> [Ссылка на проект в Jenkins](https://jenkins.autotests.cloud/job/litres_autotest_project/)

#### Параметры сборки

- `browser-version` - версия браузера (браузер `Chrome`)
- `comment` - комментарий


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
#### Список тест кейсов
![This is an image](media/images/allure_report.png)
#### Пример отчета о прохождении теста
![This is an image](media/images/example_test_ui_allure.png)

----
### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> [Ссылка на проект в AllureTestOps](https://allure.autotests.cloud/project/3942/dashboards) (запрос доступа `admin@qa.guru`)

#### Тест-планы проекта
![This is an image](media/images/allure_TestOps_test_plans.png)

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](media/images/allure_TestOps_test_cases.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](media/images/example_autotests_allure_TestOps.png)

#### Тестовые артефакты
![This is an image](media/images/allure_TestOps_attachment.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](media/images/allure_TestOps_dashboard.png)

#### История запуска тестовых наборов
![This is an image](media/images/allure_TestOps_launches.png)

----
### Интеграция с Jira
> [Ссылка на проект в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1045)

![This is an image](media/images/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](media/images/tg_notification.png)

----
### Пример видео прохождения ui-автотеста
![autotest_gif](media/images/autotest.gif)

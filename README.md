# Фреймворк для автоматизации тестирования сайта "Softmg.ru"

  <a target="_blank" href="https://Softmg.ru/">
    <img title="softmg_logo_2" alt="Logo" src="/data_image_from_readme/softmg_logo_2.png" height="400" width="1920"/>
  </a>

----


### Table of Contents 🤸


- [Особенности проекта ](#about_project)

- [Список проверок](#list_test)

- [Используемый стэк](#stack)

- [Локальный запуск автотестов 🧙‍♂️](#local_start_project)
    - [Запуск 🦧](#start_test)
    - [Получение отчёта 🧑‍💻](#allure_serve)

- [Отчет в Jenkins 🪄](#project_in_jenkins)
     - [Параметры сборки 🦧](#param_in_jenk)
     - [Запуск 🧑‍💻](#start_test_jenk)

- [Allure отчет 🪄](#allure_report)

- [Оповещения 🪄](#notification_tg)

- [Видео 🪄](#video)

----

<img title="softana" align="left" src="data_image_from_readme/softana_2.png" height="500" width="300"/> 

----


### <a name="about_project">Особенности проекта</a>

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Запуск web/UI автотестов в Selenoid
* Запуск тестов на dev и prod контурах

### <a name="list_test">Список проверок, реализованных в web/UI автотестах</a>

- [x] Проверки линков на всех страницах
- [x] Проверка успешной отправки заявки
- [x] Проверка негативных кейсов отправки заявок
- [x] Проверка работоспособности меню (включая вложенность)


----

### <a name="stack">Используемый стэк</a>

<img title="Python" src="data_image_from_readme/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="data_image_from_readme/icons/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="data_image_from_readme/icons/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="data_image_from_readme/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="data_image_from_readme/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="data_image_from_readme/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="data_image_from_readme/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="data_image_from_readme/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="data_image_from_readme/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="data_image_from_readme/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="data_image_from_readme/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="data_image_from_readme/icons/jenkins-original.svg" height="40" width="40"/>


----

### <a name="local_start_project">Локальный запуск автотестов</a>

#### <a name="start_test">Запуск тестов:</a>
Для запуска web/UI автотестов выполнить в cli:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```
Для получения отчета выполнить в cli:
#### <a name="allure_serve">Получение отчёта:</a>
```bash
allure allure serve
```

----

### <a name="project_in_jenkins">Проект в Jenkins</a>
> <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/">Ссылка</a>


#### <a name="param_in_jenk">Параметры сборки</a>
```python
ENVIRONMENT = ['development', 'PROD_PAGE'] # Окружение
BROWSER_VERSION = '127.0' # Версия браузера хром. Можно запускать на 128.0
```
#### <a name="start_test_jenk">Запуск автотестов в Jenkins</a>
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/">проект</a>

![jenkins project main page](/data_image_from_readme/jenkins_project_main_page.png)

1. Нажать "Build with Parameters"
2. Из списка "ENVIRONMENT" выбрать окружение
3. В поле "BROWSER_VERSION" ввести версию браузера (запуск возможен в 128.0 и 127.0 версиях)
4. Нажать "Build"

![jenkins_build](/data_image_from_readme/start_job_in_jenkins.png)

----

### <a name="allure_report">Allure отчет</a>

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/">Открытие отчета после сборки</a>
![allure_report_after_work_job](/data_image_from_readme/allure_report_after_work_job.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/24/allure/">Общие результаты</a>
![allure_report_overview](/data_image_from_readme/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](/data_image_from_readme/allure_reports_behaviors.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/24/allure/#graph">Графики</a>


![allure_reports_graphs](/data_image_from_readme/allure_reports_graphs_1.png)
![allure_reports_graphs](/data_image_from_readme/allure_reports_graphs_2.png)


----

### <a name="notification_tg">Оповещения в Telegram</a>
![telegram_allert](/data_image_from_readme/telegram_allert.png)

----

### <a name="video">Видео прохождения web/UI автотеста</a>
![autotest_gif](/data_image_from_readme/autotest.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
----

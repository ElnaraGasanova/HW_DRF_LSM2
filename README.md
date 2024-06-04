## Домашняя работа 24-26. "Основы веб-разработки на Django".
```
https://github.com/ElnaraGasanova/HW_DRF_LSM2.git
```
Приложение для онлайн-обучения, платформа LMS-системы, в которой каждый желающий
может размещать свои полезные материалы или курсы.
В приложении можно создать/изменить/удалить Пользователя, Курс, Лекции, Подписку на обновление курса,
Оплату курса/урока. Пользователи, которые не заходили на платформу более 30 дней - блокируются.
Реализована фильтрация вывода списка платежей по дате оплаты, по курсу или уроку, способу оплаты.
Реализовано разграничение прав доступа для Пользователей. Осуществлена проверка на отсутствие
в материалах ссылок на сторонние ресурсы, кроме youtube.com. Реализовали функционал подписки асинхронной рассылку писем
пользователям писем об обновлении материалов курса: раз в день/неделю/месяц. Вся информация сохраняется в БД PostgreSQL.
В проекте описан Dockerfile для запуска контейнера с проектом. В Docker Compose Django описан проект с БД PostgreSQL,
работа с Redis и Celery.
Для работы с периодическими задачами (ОС Windows) использована библиотека apscheduler.
Документация находится по адресу:
```commandline
https://pypi.org/project/django-apscheduler/
```
Документация Redis находится по адресу (!запускать с применением VPN):
```commandline
https://redis.io/docs/latest/
```

### Используемые технологии:
* Python
* Django
* PostgerSQL
* WSL
* Redis
* Celery
* Stripe
* Apscheduler
* Docker Desktop

#### Параметры по работе в БД с Пользователями:
* Email Пользователя
* Номер телефона Пользователя
* Город проживания Пользователя
* Аватар Пользователя

#### Параметры по работе в БД с Курсами:
* Наименование курса
* Превью курса
* Описание
* Автор курса

#### Параметры по работе в БД с Уроками:
* Наименование урока
* Наименование курса, к которому привязан урок
* Превью урока
* Описание
* Ссылка на видео урока
* Автор урока

#### Параметры по работе в БД с Подпиской на обновление курса:
* Пользователь подписки
* Курс в подписке
* Активность подписки

#### Параметры по работе в БД с Платежами:
* Плательщик (Пользователь курса)
* Дата оплаты курса/урока
* Указание курса/урока, который был оплачен
* Сумма оплаты
* Способ оплаты
* Ссылка на оплату
* ID Сессии

### ИНСТРУКЦИЯ ПО РАЗВЕРТЫВАНИЮ
* Сделайте Fork этого репозитория. Репозиторий появится
в личных репозиториях на GitHub:
```
https://github.com/ElnaraGasanova/HW_DRF_LSM2.git
```
* Сделайте git clone форкнутого репозитория, чтобы получить
репозиторий локально:
```
git clone https://github.com
```
* Создайте виртуальное окружение и активируйте его:
```
python -m venv venv
venv\Scripts\activate
```
p.s. Для выхода из виртуального окружения и возврата к глобальному
окружению Python введите следующую команду:
```
deactivate
```
* Для установки всех библиотек выполните команду:
```
pip install -r requirements.txt
```
* Для соединения с pgAdmin внесите информацию о пароле в config/settings.py в 
разделе DATABASES = ...

* Создайте файл .env по образцу файла .env.sample и заполните все данные

* Приложение работает следующим образом, для соединения с сервером,
необходимо в терминале PyCharm ввести команду:
```
python manage.py runserver
```
* Запустить окно WSL, в нем запустить redis и проверить работоспособность командами:
```
service redis-server start
redis-cli ping
"в ответ должно вернуться PONG"
```
* В двух других новых окнах терминале PyCharm запускаем celery командами:
```
celery -A django_drf worker —loglevel=info
celery -A django_drf beat —loglevel=info
```
* и перейти по ссылке для дальнейшей работы
```
http://127.0.0.1:8000/
```
* Запуск контейнера с проектом, необходимо в терминале PyCharm ввести команду:
```
docker-compose up -d --build
```
* Перейти в приложение Docker Desktop, где запустился наш проект и далее по ссылке подключения
```
http://localhost:8000/
```
### Автор проекта
```
https://github.com/ElnaraGasanova
```
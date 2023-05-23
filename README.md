# api_yamdb


![Django REST workflow](https://github.com/MaryMash/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание:
### REST API для YaMDb
YaMDb - платформа, созданная для комментирования и выставления оценок различным произведениям художественной литературы, кино и музыки. 

## Технологии
- Python 3.7
- Django 2.2.16
- Django Rest Framework 3.12.4
- PostgreSQL
- Nginx
- Gunicorn
- Docker
- Docker Compose

## Запуск проекта:

Для запуска проекта необходимо проделать следующие действия:

* Клонировать репозиторий и перейти в него в командной строке;

```
git clone git@github.com:kultmet/api_yamdb.git
```

```
cd infra_sp2
```

* В директории /infra создать файл .env. Пример заполнения:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```

* Запустить контейнер;

```
docker-compose up -d
```

* Выполнить миграции

```
docker-compose exec web python manage.py migrate
```
* Создать суперпользователя

```
docker-compose exec web python manage.py createsuperuser
```

* Собрать статику

```
docker-compose exec web python manage.py collectstatic --no-input 
```

* Скопировать в контейнер файл с фикстурами для загрузки в БД:

```
docker cp fixtures.json infra_web_1:app/
```

* Загрузить данные в базу:

```
docker-compose exec web python manage.py loaddata fixtures.json
```

Проект должен быть доступен по адресу http://localhost/admin. 

#Доска объявлений


##Технологии использованные в проекте
- Python 3.12
- Django 5.0.6
- DRF 3.15.2
- PostgreSQL
- Docker

##Функции
- авторизация и аутентификация пользователей
- распределение ролей между польщзователями (пользователь и админ)
- восстановление пароля через электронную почту
- создание, редактирование, просмотр и удаление объявлений
- добавление и просмотр отзывов к объявлениям
- разграничение прав доступа (админ может удалять или редактировать все объявления и отзывы, а пользователь может удалять и редактировать только свои объявления и комментарии


##Инструкция по развертыванию проекта
**<span style="color:green">Клонировать репозиторий:</span>**

```
git@github.com:petrovi-4/notice_board.git
```

###<span style="color:red">Из Docker контейнера</span>

**<span style="color:green">Настройка окружения</span>**

Создайте файл `.env.docker` на основе примера `.env_docker` и заполните его необходимыми данными

```
cp .env_docker .env.docker
```

**<span style="color:green">Запуск контейнера</span>**

```
docker-compose up -d —build 
```

**<span style="color:green">Загрузка фикстур(по желанию)</span>**

После успешного запуска контейнеров можно загрузить тестовые данные(фикстуры) в базу данных

```
docker-compose exec app python manage.py loaddata user_data.json
docker-compose exec app python manage.py loaddata ad_data.json
docker-compose exec app python manage.py loaddata comment_data.json
```

**<span style="color:green">Остановка контейнера</span>**

```
docker-compose down
```


###<span style="color:red">Без Docker</span>

**<span style="color:green">Создать и активировать виртуальное окружение:</span>**

```
python3 -m venv env         (для Unix-систем)
source env/bin/activate     (для Unix-систем)
```
```
python -m venv env          (для Windows-систем)
env/Scripts/activate.bat    (для Windows-систем)
```

**<span style="color:green">Настройка окружения</span>**

Создайте файл `.env` на основе примера `.env_sample` и заполните его необходимыми данными

```
cp .env_sample .env
```

**<span style="color:green">Установка зависимостей из файла requirements.txt:</span>**

```
python3 -m pip install --upgrade pip    (для Unix-систем)
python -m pip install --upgrade pip     (для Windows-систем)
```
```
pip install -r requirements.txt
```

**<span style="color:green">Выполнить миграции:</span>**

```
python3 manage.py migrate   (для Unix-систем) 
python manage.py migrate    (для Windows-систем)
```

**<span style="color:green">Запуск проекта:</span>**

```
python3 manage.py runserver (для Unix-систем)
python manage.py runserver  (для Windows-систем)
```

**<span style="color:green">Загрузка фикстур(по желанию)</span>**

После успешного запуска проекта можно загрузить тестовые данные(фикстуры) в базу данных

```
python manage.py loaddata user_data.json
python manage.py loaddata ad_data.json
python manage.py loaddata comment_data.json
```

###**<span style="color:red">Документация API:</span>**

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```


**<span style="color:maroon">Автор</span>**  
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)


## Описание
Тестовое задание.

### О проекте
Проект, представляет собой систему регистрации, аутентификации и авторизации.

### Технологии
- **Python - 3.9**
- **Django - 4.2.7**
- **DRF - 3.14.0**
- **PostgreSQL - 15.1**

### Автор
- [Николай Петров](https://github.com/NikolayPetrow23)

## Для запуска проекта вам понадобится:

### Клонирование репозитория:

```bash
git clone git@github.com:NikolayPetrow23/auth_django_test.git
```

### Cоздать и активировать виртуальное окружение:
```
python -m venv venv

# Если у вас Linux/macOS

    source venv/bin/activate

# Если у вас windows

    source venv/scripts/activate

```
### Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Создание БД PostgreSQL с помощью Docker:
```bash
docker run -p 5432:5432 --name "Имя вашей БД" -e POSTGRES_USER="Введите пользователя для БД" -e POSTGRES_PASSWORD="Введите пароль для БД" -e POSTGRES_DB="Имя вашей БД" -d postgres:13.3
```

### Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```

### Запустить проект:
```
python manage.py runserver
```

### Создать суперпользователя:
```
python manage.py createsuperuser
```

## Примеры запросов и ответов к API

### Регистрация
#### Endpoint
```
POST  /users/signup/
```
#### Пример запроса
```
{
    "usrname": "user",
    "email": "user@mail.ru",
    "first_name": "Пользователь",
    "password": "testuser123"
}
```
#### Пример ответа
```
{
    "usrname": "user",
    "email": "user@mail.ru",
    "first_name": "Пользователь"
}
```

### После этого вам придет сообщение на почту в данном случае на user@mail.ru типа:
```
Код активации: 123234
```

### Подтвердить почту
#### Endpoint
```
POST  /users/email_verification/
```

#### Пример запроса 
```
{
    "username": "user",
    "otp_code": "123234"
}
```

#### Пример ответа
```
{
    "detail": "Почта успешно подтверждена!"
}
```

### Аутентификация
#### Endpoint
```
POST  users/token/
```

#### Пример запроса 
```
{
    "username": "user",
    "password": "testuser123"
}
```

#### Пример ответа
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDM4OTkyMywiaWF0IjoxNzAwMzAzNTIzLCJqdGkiOiI1MTk4NzRiYWVkMGU0OTFhYjhkNmU3NmE3YTNjYjE1NyIsInVzZXJfaWQiOiJuaWtvbGF5cGV0cm93MTNAbWFpbC5ydSJ9.900OjHHSZysHvVE28bbd5hy3D7uym0x36Db6NmiCNfE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzA3MTIzLCJpYXQiOjE3MDAzMDM1MjMsImp0aSI6IjAwYjE5ZTM4ZmNkYjRlYTJiMmU3YjU4N2JiMzU1MDgxIiwidXNlcl9pZCI6Im5pa29sYXlwZXRyb3cxM0BtYWlsLnJ1In0.BU9xtQEJMvhjiEBegXSPn1M2u1EwVo7dWcMC4bh2-_0"
}
```

### Узнать свои данные
#### Endpoint.
```
GET  /users/me/
```

#### Пример ответа
```
{
    "username": "user",
    "first_name": "Пользвоатель",
    "email": "user@mail.ru"
}
```

### Изменить свои данные
#### Endpoint
```
PATCH  /users/me/
```

#### Пример запроса.
```
{
    "username": "user1"
}
```

#### Пример ответа.
```
{
    "username": "user1",
    "first_name": "Пользвоатель",
    "email": "user@mail.ru"
}
```

### Удалить свою учетную запись
#### Endpoint
```
DELETE  /users/me/
```

#### Пример ответа.
```
{
    "detail": "Учетная запись была успешно удалена!"
}
```

### Обновление токена
#### Endpoint
```
POST /token/refresh/
```

#### Пример запроса.
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDM4OTkyMywiaWF0IjoxNzAwMzAzNTIzLCJqdGkiOiI1MTk4NzRiYWVkMGU0OTFhYjhkNmU3NmE3YTNjYjE1NyIsInVzZXJfaWQiOiJuaWtvbGF5cGV0cm93MTNAbWFpbC5ydSJ9.900OjHHSZysHvVE28bbd5hy3D7uym0x36Db6NmiCNfE"
}
```

#### Пример ответа.
```
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzA4MjA2LCJpYXQiOjE3MDAzMDQ2MDYsImp0aSI6ImMxYzczNTkwYmEzNjQ0MWNhZDEzODQ3NDJlZDYzYmMxIiwidXNlcl9pZCI6Im5pa29sYXlwZXRyb3cxMzIzMTIzQG1haWwucnUifQ.WpmzwBgyL7bgfdD2i1Olo3OehjeRp7g9fnIYrH9DgvI"
}
```

### Проверка токена
#### Endpoint
```
POST /token/verify/
```

#### Пример запроса.
```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzA4MjA2LCJpYXQiOjE3MDAzMDQ2MDYsImp0aSI6ImMxYzczNTkwYmEzNjQ0MWNhZDEzODQ3NDJlZDYzYmMxIiwidXNlcl9pZCI6Im5pa29sYXlwZXRyb3cxMzIzMTIzQG1haWwucnUifQ.WpmzwBgyL7bgfdD2i1Olo3OehjeRp7g9fnIYrH9DgvI"
}
```

#### Пример ответа.
```
{
    "detail": "Token is valid"
}
```
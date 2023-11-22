
## Description
Test task.

### About the project
This project is a system of registration, authentication and authorization.

### The project is located at: https://testauth.ddns.net/

### Project documentation: swagger - https://testauth.ddns.net/swagger/

### Openapi project documentation - https://testauth.ddns.net/redoc/

### Technologies
- **Python - 3.9**
- **Django - 4.2.7**
- **DRF - 3.14.0**
- **PostgreSQL - 15.1**

### Author
- [Николай Петров](https://github.com/NikolayPetrow23)

## To start the project, you will need:

### Cloning the repository:

```bash
git clone git@github.com:NikolayPetrow23/auth_django_test.git
```

### Create and activate a virtual environment:
```
python -m venv venv

# If you have Linux/macOS

    source venv/bin/activate

# If you have windows

    source venv/scripts/activate

```
### Install dependencies from a file requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Creating a PostgreSQL database using Docker:
```bash
docker run -p 5432:5432 --name "Name of your database" -e POSTGRES_USER="Enter the user for the database" -e POSTGRES_PASSWORD="Enter the password for the database" -e POSTGRES_DB="Name of your database" -d postgres:13.3
```

### Perform migrations:
```
python manage.py makemigrations
python manage.py migrate
```

### Launch a project:
```
python manage.py runserver
```

### Create a superuser:
```
python manage.py createsuperuser
```

## Deploying the project to servers

### Cloning the repository to the server:
```bash
git clone git@github.com:NikolayPetrow23/auth_django_test.git
```

### Need to make an external nginx configuration file:
```
# There is an example in the repository
# You also need to install a screenshot to get a certificate with the following commands:
sudo apt install snapd

# Installing and updating dependencies for the snap package manager.
sudo snap install core; sudo snap refresh core
# If the dependencies are successfully installed, the terminal will display:
# core 16-2.58.2 from Canonical✓ installed 

# Installing the certbot package.
sudo snap install --classic certbot
# Upon successful installation of the package, the terminal will display:
# certbot 2.3.0 from Certbot Project (certbot-eff✓) installed

# Creating a link to certbot in the system directory,
# so that a user with administrator rights has access to this package.
sudo ln -s /snap/bin/certbot /usr/bin/certbot 

# Launching a serbot
sudo certbot --nginx 

# The domain can be taken on this site: https://my.noip.com/
```

### In the root folder of the project, build and install all dependencies and containers:
```bash
docker-compose build
```

### Launch containers:
```bash
docker-compose up
```

## Examples of API requests and responses

### Registration
#### Endpoint
```
POST  /api/v1/users/signup/
```
#### Request example
```
{
    "usrname": "user",
    "email": "user@mail.ru",
    "first_name": "User",
    "password": "testuser123"
}
```
#### Sample response
```
{
    "usrname": "user",
    "email": "user@mail.ru",
    "first_name": "User"
}
```

### After that, you will receive an email in this case to user@mail.ru like:
```
Activation code: 123234
```

### Confirm Email
#### Endpoint
```
POST  /api/v1/users/email_verification/
```

#### Request example
```
{
    "username": "user",
    "otp_code": "123234"
}
```

#### Sample response
```
{
    "detail": "Mail has been successfully confirmed!"
}
```

### Authentication
#### Endpoint
```
POST  /api/v1users/token/
```

#### Request example
```
{
    "username": "user",
    "password": "testuser123"
}
```

#### Response example
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDM4OTkyMywiaWF0IjoxNzAwMzAzNTIzLCJqdGkiOiI1MTk4NzRiYWVkMGU0OTFhYjhkNmU3NmE3YTNjYjE1NyIsInVzZXJfaWQiOiJuaWtvbGF5cGV0cm93MTNAbWFpbC5ydSJ9.900OjHHSZysHvVE28bbd5hy3D7uym0x36Db6NmiCNfE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzA3MTIzLCJpYXQiOjE3MDAzMDM1MjMsImp0aSI6IjAwYjE5ZTM4ZmNkYjRlYTJiMmU3YjU4N2JiMzU1MDgxIiwidXNlcl9pZCI6Im5pa29sYXlwZXRyb3cxM0BtYWlsLnJ1In0.BU9xtQEJMvhjiEBegXSPn1M2u1EwVo7dWcMC4bh2-_0"
}
```

### Find out your details
#### Endpoint.
```
GET  /api/v1/users/me/
```

#### Sample response
```
{
    "username": "user",
    "first_name": "User",
    "email": "user@mail.ru"
}
```

### Change your data
#### Endpoint
```
PATCH  /api/v1/users/me/
```

#### Request example.
```
{
    "username": "user1"
}
```

#### Sample response.
```
{
    "username": "user1",
    "first_name": "User",
    "email": "user@mail.ru"
}
```

### Delete your account
#### Endpoint
```
DELETE  /api/v1/users/me/
```

#### Sample response.
```
{
    "detail": "The account has been successfully deleted!"
}
```

### Token Update
#### Endpoint
```
POST /api/v1/token/refresh/
```

#### Request example.
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDM4OTkyMywiaWF0IjoxNzAwMzAzNTIzLCJqdGkiOiI1MTk4NzRiYWVkMGU0OTFhYjhkNmU3NmE3YTNjYjE1NyIsInVzZXJfaWQiOiJuaWtvbGF5cGV0cm93MTNAbWFpbC5ydSJ9.900OjHHSZysHvVE28bbd5hy3D7uym0x36Db6NmiCNfE"
}
```

#### Sample response.
```
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzA4MjA2LCJpYXQiOjE3MDAzMDQ2MDYsImp0aSI6ImMxYzczNTkwYmEzNjQ0MWNhZDEzODQ3NDJlZDYzYmMxIiwidXNlcl9pZCI6Im5pa29sYXlwZXRyb3cxMzIzMTIzQG1haWwucnUifQ.WpmzwBgyL7bgfdD2i1Olo3OehjeRp7g9fnIYrH9DgvI"
}
```

### Token verification
#### Endpoint
```
POST /api/v1/token/verify/
```

#### Request example.
```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzA4MjA2LCJpYXQiOjE3MDAzMDQ2MDYsImp0aSI6ImMxYzczNTkwYmEzNjQ0MWNhZDEzODQ3NDJlZDYzYmMxIiwidXNlcl9pZCI6Im5pa29sYXlwZXRyb3cxMzIzMTIzQG1haWwucnUifQ.WpmzwBgyL7bgfdD2i1Olo3OehjeRp7g9fnIYrH9DgvI"
}
```

#### Sample response.
```
{
    "detail": "Token is valid"
}
```
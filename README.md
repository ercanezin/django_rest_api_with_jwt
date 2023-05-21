# Rest API with Simple JWT in Django

This application is developed to fulfill the requirements for a Simple
Rest Application that is able to; 

* Register a new user
* Login user and retrieve a refresh and access token
* Renew Access Token
* Get Login Logs 

# Tech Stack
 
**Server:** Django 4, Python 3.11, REST Architecture

**DB:** MySQL

**Documentation:** Provided Here

**Required Libraries**
    `Django` 4.2.1, 
    `djangorestframework` 3.14.10,
    `djangorestframework-simplejwt` 5.2.2,
    `mysqlclient` 2.11.1


# To install project

Installing project is fairly simple. 
Please download the project(via git clone) or extract the zip/rar if it is the provided form. 

Navigate to the root directory of the project and run following command to make sure all libraries are installed. 

Make sure you have Python 3.11 if you don't please install it.
Once you install Python 3.11, now create a virtual environment with the following command: 

```bash
   python3 -m venv .venv
```
 After creating the virtual environment, activate it by running following:

```bash
   source .venv/bin/activate
```

This will change the prefix of your current bash program to (.venv). After activating the environment
navigate to the root of the project and run the following command to install required libraries for the project:

```bash
   pip install -r requirements.txt
```

This will install all required libraries to your .venv environment. 

Now you need to make sure you have `MySQL Server` up and running in your local or remote computer.

Update following lines in `settings.py` file to make sure you can establish a test connection. 
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'integration_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```
The project expect a database called `integration_db` to be in `MySQL Server`, if you don't have one or prefer a different db to populate default data and login logs to be recorded, change it in settings file accordingly.
Run following SQL command to create a new schema/db in `MySQL Server`:

```sql
CREATE SCHEMA `integration_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;
```

Once all the steps above is done, you need to set up the project. First of all run:

```bash
python3 manage.py makemigrations
```
This will create necessary migrations locally, then run following command to save them to DB:

```bash 
python3 manage.py migrate
```

Once all migrations are done successfully, Now you are ready to run the server locally. 

Run following command to start the server:

```bash
python3 manage.py startserver
```

Once your server is up and running successfully, you are ready to test out Rest API.

 
## API Reference

#### Register a new user

```http
  POST api/v1/auth/register/
```

| Parameter     | Type         | Description                                      |
|:--------------|:-------------|:-------------------------------------------------|
| `username`    | `charField`  | **Not Required**. String for the field.          |
| `password`    | `charField`  | **Required**. Valid Strong String for the field. |
| `re_password` | `charField`  | **Required**. Valid Strong String for the field. |
| `email`       | `emailField` | **Required**.  Valid Email String for the field. |
| `first_name`  | `charField`  | **Not Required**.  String for the field.         |
| `last_name`   | `charField`  | **Not Required**.    String for the field.       |

#### Login to Rest API and get tokens

```http
  POST api/v1/auth/login/
```

| Parameter  | Type        | Description                                      |
|:-----------|:------------|:-------------------------------------------------|
| `username` | `charField` | **Required**. String for the field.              |
| `password` | `charField` | **Required**. Valid Strong String for the field. |

* returns `refresh` and `access` tokens in JSON Format. 

#### Update an access token 

```http
  POST /api/v1/auth/token/refresh/
```

| Parameter | Type     | Description                                       |
|:----------|:---------|:--------------------------------------------------|
| `refresh` | `string` | **Required**. String for the refresh token field. | 


#### Get user login logs

```http
  GET /api/v1/users/<int:user_id>/login-logs
```
* returns  login logs of user on JSON format. 






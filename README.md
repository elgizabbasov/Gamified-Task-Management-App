# Gamified-Task-Management-App

# Task Manager
Welcome to Task Manager!

Here you are able to track your tasks and goals easily!

Was developed using Python 3.10.9, Django 4.1.7 and @vue/cli 5.0.8.

# Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/elgizabbasov/Gamified-Task-Management-App.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv myenv
$ source myenv/bin/activate
```

Then install the dependencies:

```sh
(myenv)$ pip install -r requirements.txt
```

Note the `(myenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

### Perform Migrations

The SQLite3 database will not be shipped with the project and needs to be initialized before first run. To do this run:

```sh
(myenv)$ python manage.py makemigrations
```

to package up the initial models into individual migration files, and

```sh
(myenv)$ python manage.py migrate
```

directly after that. This will apply the initial models into the database. 

### Create a Superuser

To access the website's admin panel, you must also create a Django super user. This can be achieved by running:
```sh
(myenv)$ python manage.py createsuperuser
```

and following the instructions after. This is required for testing the adding and viewing of tasks.

```sh
(myenv)$ python manage.py runserver
```

And navigate to the host address presented in the terminal. (Often `http://127.0.0.1:8000/`).

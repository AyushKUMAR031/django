# Django Command-Line

- This document provides a quick reference to the most commonly used `django-admin` and `manage.py` commands in Django development.


- **`django-admin` vs. `manage.py`**

    - **django-admin**: The main command-line utility for administrative tasks. It should be on your system path if you installed Django correctly.

    - **manage.py**: A thin wrapper around `django-admin` that is automatically created in each Django project. It sets the `DJANGO_SETTINGS_MODULE` environment variable to point to your project's `settings.py` file. For project-specific tasks, it's best practice to use `manage.py`.


## Common Commands

- `django-admin startproject myproject`  
  Create a new Django project.

- `python manage.py startapp myapp`  
  Create a new app inside the project.

- `python manage.py makemigrations`  
  Generate migrations from model changes.

- `python manage.py migrate`  
  Apply migrations to the database.

- `python manage.py createsuperuser`  
  Create an admin user for the Django admin.

- `python manage.py runserver`  
  Start the development server.

- `python manage.py shell`  
  Open a Python shell with project context.

- `python manage.py collectstatic`  
  Collect static files to `STATIC_ROOT`.

- `python manage.py test`  
  Run tests in your project.

- `python manage.py changepassword <username>`  
  Change a user's password.

- `python manage.py flush`  
  Delete all data and reset the database.

- `python manage.py dumpdata`  
  Export data as JSON.

- `python manage.py loaddata`  
  Import data from JSON fixtures.

## Help Center

- `python manage.py help`  
  List all available commands.

- `python manage.py help <command>`  
  Get help for a specific command.

# Getting Started with Django

This guide will walk you through the initial setup of a Django project, from installation to creating your first app.

## Step 1: Prerequisites

Before you begin, you need to have **Python** installed on your system. Django is a Python web framework, so Python is a hard requirement.

You can check if you have Python installed by opening your terminal or command prompt and running:

```bash
python --version
```

If you don't have Python, you can download it from the official website: [python.org](https://www.python.org/downloads/)

## Step 2: Setting up a Virtual Environment

A virtual environment is a self-contained directory that holds a specific version of Python and its packages. It's a best practice to use a virtual environment for every project to avoid conflicts between project dependencies.

1.  **Create a virtual environment:**
    Navigate to your project folder in the terminal and run the following command. We'll name our environment `.venv`.

    ```bash
    python -m venv .venv
    ```

2.  **Activate the virtual environment:**

    - **On Windows:**
      ```bash
      .\.venv\Scripts\activate
      ```
    - **On macOS and Linux:**
      ```bash
      source .venv/bin/activate
      ```

    Once activated, you'll see the name of the virtual environment in your terminal prompt (e.g., `(.venv) C:\Users\YourUser\project>`).

## Step 3: Installing Django

With your virtual environment activated, you can now install Django using `pip`, Python's package installer.

```bash
pip install django
```

This command will download and install the latest stable release of Django.

## Step 4: Creating a Django Project

Now that Django is installed, you can create a new project. A Django project is a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings.

Run the following command to create a project named `myproject`. You can replace `myproject` with any name you like. The `.` at the end tells the script to create the project in the current directory.

```bash
django-admin startproject myproject .
```

After running this command, you will see a new directory `myproject` and a file `manage.py` in your project folder.

### Understanding the Project Structure

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You'll use it to run the development server, create apps, run database migrations, and more.
- `myproject/`: The project's Python package.
  - `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
  - `settings.py`: Contains all the settings and configuration for your project.
  - `urls.py`: The URL declarations for this Django project; a "table of contents" of your site.
  - `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.
  - `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.

## Step 5: Running the Development Server

Django comes with a lightweight development server to test your project.

1.  **Run the server:**
    Make sure you are in the same directory as `manage.py` and run:

    ```bash
    python manage.py runserver
    ```

2.  **View your site:**
    Open a web browser and go to `http://127.0.0.1:8000/`. You should see a "Congratulations!" page, which means your Django project is working correctly.

3.  **Stopping the server:**
    To stop the development server, go back to your terminal and press `Ctrl+C`.

## Step 6: Create the `apps` Directory

To keep our project organized, we will create a dedicated directory to hold all of our applications.

```bash
# Create the 'apps' directory
mkdir apps

# Create an __init__.py file to make it a Python package
touch apps/__init__.py
```

## Step 7: Creating a Django App

In Django, a project is a collection of applications (or "apps"). An app is a web application that does something – e.g., a weblog system, a database of public records, or a simple poll app. A project can contain multiple apps.

1.  **App creation:**
    To create an app, use the `manage.py` utility. Let's create an app named `myapp`.

    ```bash
    python manage.py startapp apps/myapp
    ```

2.  **App Structure:**
    This will create a new directory named `myapp` with the following files:

    - `__init__.py`: Marks the directory as a Python package.
    - `admin.py`: Configuration for the Django admin interface.
    - `apps.py`: Configuration for the application itself.
    - `models.py`: Where you define your application's database models.
    - `tests.py`: Where you write your tests.
    - `views.py`: Where you write your application's views (the logic that handles requests and returns responses).
    - `migrations/`: A directory that stores database migration files.

3.  **Install the app:**
    For your project to know about the new app, you need to add it to the `INSTALLED_APPS` list in your project's `settings.py` file.

    Open `myproject/settings.py` and add `'myapp'` to the `INSTALLED_APPS` list:

    ```python
    # myproject/settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myapp',  # Add this line
    ]
    ```

## Step 8: Create the "Hello_world." View

Now we'll create a simple view to display our message.

1.  **Create the view.** Open `apps/hello_world/views.py` and add the following code:

    ```python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world.")
    ```

2.  **Create the app's `urls.py`.** Create a new file `apps/hello_world/urls.py` and add the following code:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.index, name="index"),
    ]
    ```

3.  **Include the app's URLs in the main project.** Open `project/urls.py` and include the `hello_world` app's URLs:

    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("hello/", include("hello_world.urls")),
        path('admin/', admin.site.urls),
    ]
    ```

## Step 9: Create `requirements.txt`

To make it easy for other developers (or your future self) to install the project's dependencies, create a `requirements.txt` file.

```bash
# Freeze the current list of installed packages into a file
pip freeze > requirements.txt
```

## Project vs. App

- **App:** An app is a module that handles a specific feature (e.g., a blog, a user authentication system). Apps are designed to be reusable across different projects.
- **Project:** A project is a collection of apps and their configurations that, together, form a complete website or application.

Think of it this way: a project is the house, and apps are the rooms within the house (living room, kitchen, bedroom).

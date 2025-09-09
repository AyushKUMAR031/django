# Unit 5: Models, Migrations, and Django Admin

### 1. Create Django Models

A Django model is a Python class that represents a database table. It's the single, definitive source of information about your data.

-   **Defining a Model:**
    -   Models are defined in your app's `models.py` file.
    -   Each model is a class that inherits from `django.db.models.Model`.
    -   Each attribute of the class represents a database field (e.g., `CharField`, `IntegerField`, `DateTimeField`).
    -   Example:
        ```python
        from django.db import models

        class Student(models.Model):
            first_name = models.CharField(max_length=30)
            last_name = models.CharField(max_length=30)
            email = models.EmailField()
        ```

-   **Registering the App:**
    -   To include the app in your project, add its configuration class to the `INSTALLED_APPS` list in your project's `settings.py`.

---

### 2. Work with Migrations

Migrations are Django's way of propagating changes you make to your models into your database schema.

-   **Creating Migrations:**
    -   Run `python manage.py makemigrations` to create new migration files based on the changes in your models.
-   **Applying Migrations:**
    -   Run `python manage.py migrate` to apply the migrations to your database. [stored in migrations folder inside the app]
-   **Viewing SQL:**
    -   Run `python manage.py sqlmigrate <app_name> <migration_name>` to see the SQL statements for a migration.
-   **Listing Migrations:**
    -   Run `python manage.py showmigrations` to see all migrations and their status.

---

### 3. Use the Django Shell

The Django shell is an interactive Python console for your Django project.

-   **Starting the Shell:**
    -   Run `python manage.py shell`.
-   **Interacting with the Database:**
    -   You can import your models and use the ORM to create, retrieve, update, and delete objects.
    -   Example:
        ```python
        from apps.studentManager.models import Student

        # Create a new student
        student = Student(first_name='John', last_name='Doe', email='john.doe@example.com')
        student.save()

        # Get all students
        students = Student.objects.all()

        # Filter students
        students = Student.objects.filter(last_name='Doe')
        students = Student.objects.filter(age__gte=18)

        # Get a single student
        student = Student.objects.get(id=1)

        # Delete a student
        student.delete()

        from django.utils import timezone
        print(timezone.now())
        ```
        ```bash
        # how shell looks
        >>> students = Student.objects.all()
        >>> students
        <QuerySet [<Student: Ayush (21)>, <Student: Itachi (22)>]>

        >>> for s in students:
        ...     print(s.name)
        ...
        ```
    - **how do shell get to know enter is for next line or run ?** -> Python REPL rules -> Read–Eval–Print–Loop

---

### 4. Understand Django ORM Basics

- The Object-Relational Mapper (ORM) allows you to interact with your database using Python code instead of SQL.
- In Django, ORM connects your models (Python classes) to your database tables.

- ORM 

-   **Querying Data:**
    -   `all()`: Retrieve all objects.
    -   `filter()`: Retrieve a subset of objects.
    -   `get()`: Retrieve a single object.
-   **Lazy Evaluation:** QuerySets are lazy. They don't hit the database until they are evaluated.

-   **QuerySet filters (very powerful)**
    - `exact` → Student.objects.filter(name__exact="Ayush")
    - `contains` → Student.objects.filter(name__contains="it")
    - `gt / gte` → greater than / greater or equal
    - `lt / lte` → less than / less or equal
    - `in` → Student.objects.filter(age__in=[18, 21, 25])
    - `startswith / endswith`

---

### 5. Define and Use Foreign Keys in Models

A `ForeignKey` creates a `many-to-one relationship` between models.

-   **Defining a Foreign Key:**
    -   Use `models.ForeignKey` in your model.
    -   The first argument is the "parent" model.
    -   The `on_delete` argument specifies what happens when the parent object is deleted (e.g., `models.CASCADE`, `models.PROTECT`, `models.SET_NULL`).
    -   Example:
        ```python
        from django.db import models

        class Course(models.Model):
            name = models.CharField(max_length=100)

        class Enrollment(models.Model):
            student = models.ForeignKey(Student, on_delete=models.CASCADE)
            course = models.ForeignKey(Course`actual classes name`, on_delete=models.CASCADE)
        ```

    - 3. Common on_delete options
        - `CASCADE` → delete related rows too.
        - `SET_NULL` → set the field to NULL if parent is deleted (requires null=True).
        - `PROTECT` → prevent deletion if related objects exist.
        - `DO_NOTHING` → do nothing (might cause database errors).

        ```python
        t1.student_set.all() #this student_set is predefined : for `all Student objects that point to this Teacher.`
        # <QuerySet [<Student: Ayush>, <Student: Itachi>]>
        ```

---

### 6. Use the Django Admin Interface

- Django provides a built-in admin interface for managing your site's content.
- It lets you manage your database (add,edit,delete records) through a web UI,without writing SQL

-   **Enabling the Admin:**
    -   Ensure `'django.contrib.admin'` is in `INSTALLED_APPS`.
    -   Include the admin URLs in your project's `urls.py`.
-   **Registering Models:**
    -   Register your models in your app's `admin.py` file to make them editable in the admin. (in app directory)
    -   Example:
        ```python
        from django.contrib import admin
        from .models import Student

        admin.site.register(Student)
        ```

    
-   **Setting Up Admin**
        ```bash
            (.venv) PS D:\master\PrimaryThings\DevBook\django> python manage.py createsuperuser
            Username (leave blank to use 'hp'): Uchiha Itachi
            Error: Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.
            Username (leave blank to use 'hp'): Uchiha_Itachi 
            Email address: ayush@gmail.com
            Password: 
            Password (again): 
            Superuser created successfully.
        ```

    
-   **Customization:**
    -   You can customize the admin interface to control how your models are displayed.
    - [see the page](./custom_admin_UI.md)

---

### 7. Add Groups and Users via Admin

Django's authentication system includes `User` and `Group` models.

-   **Users:** Individual accounts with permissions.
-   **Groups:** A way to categorize users and apply permissions to them collectively.
-   You can manage users and groups through the Django admin interface.

### 8. Set Up User Permissions in Admin

Django has a built-in permission system.

-   **Default Permissions:** Django automatically creates `add`, `change`, `delete`, and `view` permissions for each model.
-   **Assigning Permissions:** You can assign permissions to users or groups in the admin interface.

### 9. Configure and Set Up the Database

-   **Database Configuration:**
    -   The `DATABASES` dictionary in `settings.py` contains the database settings.
-   **Supported Databases:**
    -   Django supports SQLite, PostgreSQL, MySQL, and Oracle.
-   **Applying Initial Migrations:**
    -   Run `python manage.py migrate` to create the necessary tables for Django's built-in apps.

---
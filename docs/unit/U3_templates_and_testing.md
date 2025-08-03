## 📘 Unit III - Templates, Debugging & Testing in Django

### 🧠 1. Introduction to Templates in Django

* A Template in Dj is a text file - often HTML with embedded Django Language.
* Templates define the frontend (HTML) part of Django apps.
* It uses Django Template Language (DTL) to dynamically render data.

**Folder Structure:**

```
/project_root/
│
├── app_name/
│   └── templates/
│       └── app_name/
│           └── file.html
```

```bash
mkdir templates
# Inside studentmanager or your app folder
mkdir templates/studentManager
```

---

### 🧠 2. Creating Templates

* You create `.html` files and render them via views using `render()`.

```python
# views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'studentManager/home.html')
```

```html
<!-- templates/studentmanager/home.html -->
<h1>Welcome to Student Manager</h1>
```

---

### 🧠 3. Django Template Language (DTL)

- It is a built-in templating system used by the dj web framework to generate dynamic html and other text-based format.

- It allows devs to define the presentation layer of a web page separately from business logic by embedding Dj-specific syntax within HTML files.

#### 🧾 Syntax Basics

* **Variables** : `{{ variable }}`
* **Tags** : `{% tag %}`

**Example:**

```html
<p>Hello, {{ username }}</p>
{% if user.is_authenticated %}
  <p>Welcome back!</p>
{% else %}
  <p>Please login</p>
{% endif %}
```

---

### 🧠 4. Using Template Tags

Some common tags:

| Tag                | Purpose              |
| ------------------ | -------------------- |
| `{% if %}`         | Conditional logic    |
| `{% for %}`        | Loops                |
| `{% url %}`        | Reverse URL lookup   |
| `{% csrf_token %}` | CSRF protection      |
| `{% extends %}`    | Template inheritance |
| `{% block %}`      | Define content block |

---

### 🧠 5. Django Variables in Templates

* Passed from `views.py` using `context`.

```python
return render(request, 'home.html', {'name': 'Itachi'})
```

```html
<p>Hi {{ name }}</p> <!-- Outputs: Hi Itachi -->
```

---

### 🧠 6. for loop and if-else statements

```python
students = ['Ayush', 'Naruto', 'Sasuke']
return render(request, 'list.html', {'students': students})
```

```html
<ul>
{% for s in students %}
  <li>{{ s }}</li>
{% endfor %}
</ul>
```

```html
{% if students %}
  <p>Total: {{ students|length }}</p>
{% else %}
  <p>No students found.</p>
{% endif %}
```

---

### 🧠 7. Dynamic Templates in Django

* Django's template can generate dynamic content by passing data through a context - a dictionary containing (key : value) pair.
* You pass data dynamically via `context`.
* `Template` Uses placeholders (like {{ username }}) to insert data from the context.

* `View` Prepares the context and renders the template.
* Example: rendering user-specific pages or lists from DB.

```python
from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()  # Fetch users from the database
    return render(request, 'user_list.html', {'users': users}) # passing dynamic content (users list)

```
```html
<!--user_list.html -->
<h2>User List</h2>
<ul>
  {% for user in users %}
    <li>{{ user.name }}</li>
  {% endfor %}
</ul>
```
---

### 🧠 8. Template Inheritance
**Base Template:**

```html
<!-- base.html -->
<html>
<head><title>{% block title %}My Site{% endblock %}</title></head>
<body>
  <header>Header</header>
  {% block content %}{% endblock %}
  <footer>Footer</footer>
</body>
</html>
```

**Child Template:**

```html
<!-- home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome Home!</h1>
{% endblock %}
```
> ✅ Template inheritance in Django is a powerful feature that allows you to create a base "skeleton" template containing the common structure and elements of your website (like headers, footers, navigation bars) that are shared across multiple pages. 

> ✅ Use inheritance to avoid repeating HTML (DRY principle).

---

### 🧠 9. Debugging Django Applications

* setting debug values is to show detailed error pages with stack traces and helpful debug info.

* Only for development phase , not for production. (exposes sensitive details)

#### ✅ Enable Debug Mode (in `settings.py`)

```python
DEBUG = True
```

#### ✅ Common Debugging Tips

* Use `print()` statements in views. `: to see the flow in console/logs.`
* Use Django error tracebacks. `:  dj debug mode shows full error logs ("traceback").`
* Use `pdb` module for breakpoints. `: stops the program right at the line and opens interactive` **`pdb -> pythonDebugger.`**

```python
import pdb; pdb.set_trace()
```

---

### 🧠 10. Testing in Django

#### 🧰 Why Test?

* Ensure your app functions correctly after changes like code updates or feature additions.
* It helps catch bugs early and prevents regressions.
* Give confidence in code quality and stability.

#### 🧪 Basic Test Setup

```bash
python manage.py test
```
* This command runs all tests in your Django project.

* It automatically finds tests in any file named `tests.py` inside your apps.

* Tests ensure your code behaves as expected.

#### ✅ Example Unit Test

```python
# tests.py inside your app
from django.test import TestCase
from django.urls import reverse

class SimpleTest(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
```
- `from django.test import TestCase`  
  Imports Django’s built-in test class for writing tests with useful assertions and test client support.

- `from django.urls import reverse`  
  Allows getting URLs by their name (`'home'`), avoiding hardcoding URLs in the test.

- `class SimpleTest(TestCase):`  
  Defines a test case class inheriting from `TestCase`. Each method inside it that starts with `test_` is run as a test.

- `def test_home_status_code(self):`  
  A test method to check something specific. Here, it tests the home page’s HTTP response.

- `response = self.client.get(reverse('home'))`  
  Uses Django’s test client (`self.client`) to simulate a GET request to the URL named `'home'`. `reverse()` resolves that URL.

- `self.assertEqual(response.status_code, 200)`  
  Asserts that the HTTP response code of the home page is `200` (OK).  
  If the response is anything else (like 404 or 500), the test will fail.

---
**Additional Notes:**  
Django tests can cover:
- **Models:** Check data behavior, validations.
- **Views:** Check if pages load correctly, data rendered.
- **Forms:** Validate input handling and errors.
- **Templates:** Verify content rendering.

*Tests help maintain app reliability as it grows and changes over time.*

---
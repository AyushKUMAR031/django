## 🔹UNIT II - Django Views and URL Mapping

This guide provides a detailed overview of how Django handles views and maps them to URLs. It covers everything from the basics of creating a view to advanced URL mapping with regular expressions.

---

#### 1. Creating Views and Mapping to URLs

##### What is a View?

In Django, a **view** is a Python function that receives a web request and returns a web response. It's the core of Django's MVT (Model-View-Template) architecture, acting as the "controller" that orchestrates the logic for handling user requests.

A view's primary responsibilities include:
- Receiving and processing the `HttpRequest` object.
- Interacting with the database (via models) or other services.
- Rendering a template with context data.
- Returning an `HttpResponse` object (e.g., HTML, JSON, redirect).

##### Basic View Example

Here’s a simple "Hello, World!" view.

```python
# in myapp/views.py
from django.http import HttpResponse

def home(request):
    """
    A basic view that returns a simple HTTP response.
    """
    return HttpResponse("Hello, Django!")
```

##### Mapping a View to a URL

To make a view accessible, you need to map it to a URL.

1.  **App-level `urls.py`**: Create a `urls.py` file in your app directory.

    ```python
    # in myapp/urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'), # Map the root URL of the app
    ]
    ```

2.  **Project-level `urls.py`**: Include your app's URL configuration in the main project `urls.py`.

    ```python
    # in project/urls.py
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('', include('myapp.urls')), # Include myapp's URLs
        path('admin/', admin.site.urls),
    ]
    ```

---

#### 2. Creating View Logic

Views can contain any Python logic needed to generate a response. A common pattern is to fetch data from the database, process it, and pass it to a template.

```python
# in myapp/views.py
from django.shortcuts import render

def greet(request):
    """
    This view retrieves a 'name' from the query parameters
    and renders it in a template.
    """
    name = request.GET.get("name", "Guest")
    context = {"name": name}
    return render(request, "greet.html", context)
```

The `render()` function is a shortcut that combines a template with a context dictionary and returns an `HttpResponse` object.

---

#### 3. HTTP Requests

Django encapsulates every request in an `HttpRequest` object, which contains useful information.

-   `request.method`: The HTTP method (`'GET'`, `'POST'`, etc.).
-   `request.GET`: A dictionary-like object containing all HTTP GET parameters.
-   `request.POST`: A dictionary-like object containing all HTTP POST parameters.
-   `request.headers`: A dictionary of all request headers.
-   `request.COOKIES`: A dictionary of all cookies.
-   `request.user`: The currently logged-in user (if using authentication).

##### Example: Handling Form Data

```python
# in myapp/views.py
from django.http import HttpResponse

def form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Anonymous')
        return HttpResponse(f"Hello, {name}! Thanks for submitting the form.")
    
    # Show a simple message for GET requests
    return HttpResponse("Please send a POST request with a 'name' field.")
```

---

#### 4. Creating Responses

Django provides several built-in response types.

-   `HttpResponse()`: The most basic response, containing raw text.
-   `render()`: Renders a template and returns an `HttpResponse`.
-   `redirect()`: Redirects to another URL.
-   `JsonResponse()`: Creates a JSON-encoded response.

##### JSON Response Example

This is useful for creating APIs.

```python
# in myapp/views.py
from django.http import JsonResponse

def api_view(request):
    """
    A simple API endpoint returning a JSON response.
    """
    data = {
        "status": "ok",
        "message": "Data fetched successfully.",
    }
    return JsonResponse(data)
```

---

#### 5. Understanding URLs

Django uses `urls.py` files to define its URL structure. The `path()` function is the most common way to define a URL pattern.

-   **Route**: The URL pattern to match (e.g., `'hello/'`).
-   **View**: The view function to call when the route matches.
-   **Name**: An optional name for the URL, allowing you to refer to it from other parts of Django (e.g., in templates).

```python
# path version
path('hello/', views.say_hello, name='say_hello')

# re_path version (for regular expressions)
from django.urls import re_path
re_path(r'^hello/$', views.say_hello, name='say_hello_re')
```

---

#### 6. Mapping URLs with Parameters

You can capture parts of the URL and pass them as arguments to your view.

##### Path Parameters

Use angle brackets to capture URL segments.

```python
# in myapp/urls.py
path('user/<int:id>/', views.user_detail, name='user_detail')

# in myapp/views.py
def user_detail(request, id):
    # The 'id' argument is automatically passed from the URL
    return HttpResponse(f"You are looking at the profile for User ID: {id}")
```

Django supports several path converters:
-   `<str:name>`: Matches any non-empty string (excluding `/`).
-   `<slug:slug>`: Matches a slug (ASCII letters, numbers, hyphens, underscores).
    - **slug** :
        - A slug is a short label for something, containing only letters, numbers, underscores or hyphens.
        - It is often used in URLs to make them readable and SEO-friendly.
        - Example: Instead of `/blog/1234`, we use `/blog/what-is-a-slug`.
-   `<uuid:uuid>`: Matches a UUID.
-   `<int:id>`: Matches an integer.

---

#### 7. Regular Expressions in URLs

For more complex URL patterns, use `re_path()` with regular expressions.

##### Example: Matching a Date

```python
# in myapp/urls.py
from django.urls import re_path

urlpatterns = [
    re_path(r'^report/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', views.report, name='report'),
]

# in myapp/views.py
def report(request, year, month, day):
    return HttpResponse(f"Report for date: {year}-{month}-{day}")
```
Here, `(?P<year>\d{4})` is a named capturing group that matches a 4-digit year and passes it as the `year` argument to the view.

---

#### 8. Error Handling

Django has built-in views for common HTTP errors.

-   **404 (Not Found)**: `django.views.defaults.page_not_found`
-   **500 (Server Error)**: `django.views.defaults.server_error`
-   **403 (Permission Denied)**: `django.views.defaults.permission_denied`
-   **400 (Bad Request)**: `django.views.defaults.bad_request`

##### Custom Error Views

You can override the default error views by defining custom handlers in your project's root `urls.py`.

```python
# in project/urls.py
handler404 = 'myapp.views.custom_404_view'
handler500 = 'myapp.views.custom_500_view'

# in myapp/views.py
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)
```
To trigger these custom views in production, you must set `DEBUG = False` in your `settings.py`.

---
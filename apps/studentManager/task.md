### 🎓 Django Mini Project: Student Manager

A minimal Django app demonstrating core concepts from Unit 1 & 2 like:
- Django Project & App structure
- Views and URL mapping
- Templates
- HTTP requests and query parameters
- Custom 404 page


## ⚙️ Configure Settings

### 5. Add App to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'apps.studentManager',
]
```

---

## 🧠 Views and Logic

### 6. Create Views in `studentManager/views.py`

```python
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

students = {
    1: {"name": "Ayush", "batch": 2024},
    2: {"name": "Itachi", "batch": 2025}
}

def home(request):
    return HttpResponse("Welcome to Student Manager!")

def student_detail(request, id):
    student = students.get(id)
    if student:
        return HttpResponse(f"Student ID {id}: {student['name']}")
    return HttpResponseNotFound("Student not found")

def search_student(request):
    name = request.GET.get('name', 'Guest')  # 'name' is query key; 'Guest' is default
    return HttpResponse(f"Search result for: {name}")

def batch_students(request, year):
    filtered = [s['name'] for s in students.values() if s['batch'] == year]
    return HttpResponse(f"Students from batch {year}: {', '.join(filtered)}")

def custom_404(request, *args, **kwargs):
    return render(request, '404.html', status=404)
```

---

## 🌐 URL Routing

### 7. Configure URLs in `studentManager/urls.py`

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/<int:id>/', views.student_detail),
    path('search/', views.search_student),
    re_path(r'^batch/(?P<year>[0-9]{4})/$', views.batch_students),
]
```

### 8. Include app URLs in `project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from studentmanager import views as sv

handler404 = sv.custom_404  # Custom 404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.studentManager.urls')),
]
```

---

## 🧾 Templates

### 9. Create Template Folder

```
studentManager/
└── templates/
    └── 404.html
```

```html
<!-- studentmanager/templates/404.html -->
<h1>404 Error</h1>
<p>Oops! Page not found.</p>
```

---

## 💻 Run Server

```bash
python manage.py runserver
```

---

## 🔍 Test URLs

| URL                    | Description               |
| ---------------------- | ------------------------- |
| `/`                    | Shows homepage            |
| `/student/1/`          | Shows student with ID=1   |
| `/search/?name=Itachi` | Query param example       |
| `/batch/2025/`         | Shows students from batch |
| `/invalid/route/`      | Triggers custom 404 page  |

---

## 🧪 Common Commands Used

```bash
# Create project
django-admin startproject djangoProject .

# Create app
django-admin startapp studentmanager

# Run server
python manage.py runserver

# Make migrations (if using models)
python manage.py makemigrations
python manage.py migrate
```

---

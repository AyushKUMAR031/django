from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# --- IGNORE ---
# | Path Variant                        | Usage                                       |
# | ----------------------------------- | ------------------------------------------- |
# | `path('', views.home)`              | No name, must hardcode URL in templates     |
# | `path('', views.home, name='home')` | You can use `{% url 'home' %}` in templates |

# if u have nam=home
# u can write in template
# <a href="{% url 'home' %}">Home</a>
# This allows you to reverse-resolve the URL later in templates or views without hardcoding the path.

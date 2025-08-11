from django.urls import path
from django.urls import re_path # re_path is used for more complex URL patterns mostly for regex matching
from . import views

urlpatterns = [
    path('calculate/<str:operation>/<int:value1>/<int:value2>/', views.calculate, name='calculate'),
    path('get_api_data/<int:id>/', views.get_api_data, name='get_api_data'),
    re_path(r'^user_profile/(?P<uname>[a-zA-Z]*)/?$', views.user_profile, name='user_profile'), # r -> for raw string
]

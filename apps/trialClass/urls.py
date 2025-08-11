from django.urls import path
from django.urls import re_path # re_path is used for more complex URL patterns mostly for regex matching
from . import views

urlpatterns = [
    path('calculate/<str:operation>/<int:value1>/<int:value2>/', views.calculate, name='calculate'),
    path('get_api_data/<int:id>/', views.get_api_data, name='get_api_data'),
    re_path(r'^user_profile/(?P<uname>[a-zA-Z]*)/?$', views.user_profile, name='user_profile'), 
    
    # r -> for raw string
    # * -> matches zero or more characters
    # + -> matches one or more characters
    # $ -> end of the string
    # ^ -> start of the string
    # P -> named group
    # <> -> captures the value in the URL
    # ? -> makes the preceding character optional

    # re_path(r'^print_id/(?P<item_id>[0-9]+)/?$', views.item_id, name='item_id'),
    re_path(r'^print_id/(?P<item_id>\d{4,6})/$', views.item_id, name='item_id'),  # another example of regex matching

    re_path(r'^empname/(?P<name>[\w-]+)/?$', views.empname, name='empname'),
    
    re_path(r'^gender/(?P<gender>male|female)/?$', views.gender, name='customer_gender'), # | -> matches either (or like thing)

    # re_path(r'^password/(?P<password>[])/?$', views.password, name='password'),  
]

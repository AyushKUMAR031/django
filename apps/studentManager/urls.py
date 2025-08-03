from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/<int:id>/', views.student_detail, name='student-detail'),
    path('search/', views.search_student, name='search-student'),
    re_path(r'^batch/(?P<year>[0-9]{4})/$', views.batch_year, name='batch-year'),
]
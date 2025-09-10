from django.urls import path
from . import views

urlpatterns = [
    path('', views.Me, name='Me'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success_view, name='feedback_success'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
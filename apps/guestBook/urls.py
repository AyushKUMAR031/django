from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestBook, name='guestBook-home'),
    path('add/', views.addMessage, name='guestBook-add'),
    path('entries/', views.viewEntries, name='guestBook-entries'),
    path('message/<int:message_id>/', views.viewMessage, name='guestBook-message'),
]

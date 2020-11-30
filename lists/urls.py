from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book')
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    # path('<int:pk>/', views.book_detail, name="book_detail")
]

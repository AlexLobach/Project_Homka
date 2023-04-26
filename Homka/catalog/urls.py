from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('catalog/', views.product_index, name="products_index"),
    #path('<int:pk>/', views.product_detail, name="product_detail"),
    path('', views.store, name='store'),
    path('<int:pk>/', views.product_detail, name= 'product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order')
]

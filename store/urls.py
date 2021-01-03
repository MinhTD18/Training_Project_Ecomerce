from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='main'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
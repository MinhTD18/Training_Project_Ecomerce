from django.urls import path

from store.models import Register
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.get_register_api, name='register')
    path('login/', views.login, name='login')
]
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


@api_view(['GET'])
def get_register_api(request):
    full_name = request.GET.get('full_name')
    user_name = request.GET.get('user_name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    phone_number = request.GET.get('phone_number')
    address = request.GET.get('address')

    data = {
        'full_name': full_name,
        'user_name': user_name,
        'email': email,
        'password': password,
        'phone_number': phone_number,
        'address': address,
    }

    return Response(data, status=status.HTTP_200_OK)




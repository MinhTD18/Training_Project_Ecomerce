from django.contrib.auth.models import User, Group
from rest_framework import serializers
from store.constant import Gender


class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=128)
    user_name = serializers.CharField(max_length=128)
    email = serializers.EmailField(allow_null=False)
    password = serializers.CharField(max_length=128)
    phone_number = serializers.IntegerField()
    address = serializers.CharField(max_length=128)


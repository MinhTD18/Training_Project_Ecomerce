from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User


class UserForgotPasswordForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)

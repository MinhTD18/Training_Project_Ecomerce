from django.db import models

# Create your models here.


class Register(models.Model):
    full_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=128)

    class Meta:
        db_table = 'tbl_users'

from django.db import models


class Gender(models.IntegerChoices):
    MALE = 1
    FEMALE = 2

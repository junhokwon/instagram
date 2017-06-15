from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=24, null=True, unique=True)
    # unique=True, 값이 유일해진다. blank=True는 모두 빈값이기에 값이 유일하지 않는다.
    def __str__(self):
        return self.nickname
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=100, unique=True, blank=False,
null=False)

    # email 필드를 필수, 고유 값으로 변경
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nickname']
   
    def __str__(self):
     return self.email
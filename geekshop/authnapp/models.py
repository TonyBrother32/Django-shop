# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name='аватар', upload_to='users', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')  
    phone = models.CharField(verbose_name='телефон', max_length=12, blank=True)
    city = models.CharField(verbose_name='город', max_length=22, blank=True)
    
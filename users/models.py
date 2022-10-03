from django.db import models

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=11, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=11, decimal_places=6, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(models.Model):
    STATUS = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор')
    ]

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, unique=True, blank=False)
    password = models.CharField(max_length=20)
    role = models.CharField(choices=STATUS, max_length=9)
    age = models.IntegerField(blank=True)
    location = models.ManyToManyField(Location)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

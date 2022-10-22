from django.contrib.auth.models import AbstractUser
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


class User(AbstractUser):
    MEMBER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    STATUS = [
            (MEMBER, 'Пользователь'),
            (ADMIN, 'Администратор'),
            (MODERATOR, 'Модератор')
    ]

    role = models.CharField(choices=STATUS, max_length=9)
    age = models.SmallIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def open_ads(self):
        return self.ads.filter(is_published=True).count()

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save()



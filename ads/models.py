from django.db import models


class Ad(models.Model):
    STATUS = [(True, 'Открыто'),
              (False, 'Закрыто')]
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)  # Допускаем пустое поле
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True, choices=STATUS)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

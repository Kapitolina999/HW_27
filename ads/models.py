from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    STATUS = [(True, 'Открыто'),
              (False, 'Закрыто')]

    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True, choices=STATUS)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='ads', null=True)
    created = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    @property
    def author_name(self):
        return f'{self.author.first_name} {self.author.last_name}'

    @property
    def category_name(self):
        return self.category.name


class Selection(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='select')
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name

from django.db import models


class Book(models.Model):
    name = models.CharField('Имя', max_length=100)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

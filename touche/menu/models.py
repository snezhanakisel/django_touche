from django.db import models

# Create your models here.


class CategorieDish(models.Model):
    name = models.CharField('Имя категории', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория еды'
        verbose_name_plural = "Категории еды"


class Dish(models.Model):
    name = models.CharField('Название блюда', max_length=30)
    description = models.TextField('Описание блюда')
    price = models.CharField('Стоимость', max_length=15)
    cat = models.ForeignKey('CategorieDish', on_delete=models.CASCADE, verbose_name='Категория еды')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = "Блюда"




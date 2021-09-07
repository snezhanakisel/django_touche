from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
from django.db import models

# Create your models here.


class Chef(models.Model):
    image = models.ImageField('Фото', upload_to='static/img/team')
    name_chef = models.CharField('Заголовок', max_length=30)
    about_chef = models.CharField('Подзаголовок', max_length=150)

    class Meta:
        verbose_name = 'Повор'
        verbose_name_plural = "Повора"

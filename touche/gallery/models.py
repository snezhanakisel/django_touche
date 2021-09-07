from django.db import models

# Create your models here.


class Categorie(models.Model):
    name = models.CharField('Имя категории', max_length=20)
    slug = models.SlugField('URL', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Gallery(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    small_image = models.ImageField('Маленькая картинка', upload_to='static/gallery')
    large_image = models.ImageField('Большая картинка', upload_to='static/gallery')
    cat = models.ForeignKey('Categorie', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title
# Generated by Django 3.2.7 on 2021-09-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0002_auto_20210905_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='image',
            field=models.ImageField(upload_to='static/img/team', verbose_name='Фото'),
        ),
    ]
# Generated by Django 3.2.14 on 2022-07-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок')),
                ('description_short', models.CharField(blank=True, max_length=200, verbose_name='Короткое описание')),
                ('description_long', models.TextField(blank=True, null=True, verbose_name='Длинное описание')),
                ('lng', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]

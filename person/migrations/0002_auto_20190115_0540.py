# Generated by Django 2.1 on 2019-01-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='person',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]

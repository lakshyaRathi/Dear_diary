# Generated by Django 4.2.4 on 2023-08-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name=''),
        ),
    ]

# Generated by Django 3.1 on 2020-08-26 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200826_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='mode',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 2.2.2 on 2020-07-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200629_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='Jobindustry',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
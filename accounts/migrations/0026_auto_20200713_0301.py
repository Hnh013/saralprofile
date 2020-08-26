# Generated by Django 2.2.2 on 2020-07-13 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20200713_0258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobexperience',
            options={'verbose_name': 'Jobexperience', 'verbose_name_plural': 'Jobexperiences'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='edudetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Education'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='jobexp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Jobexperience'),
        ),
    ]

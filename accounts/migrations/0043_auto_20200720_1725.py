# Generated by Django 2.2.2 on 2020-07-21 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20200720_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ssavedresume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aplid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.applicant')),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employer')),
            ],
            options={
                'verbose_name': 'Ssavedresume',
                'verbose_name_plural': 'Ssavedresumes',
            },
        ),
        migrations.DeleteModel(
            name='savedresume',
        ),
    ]
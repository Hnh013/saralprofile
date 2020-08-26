# Generated by Django 2.2.2 on 2020-07-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_savedjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('plan_id', models.CharField(choices=[('499 per month', '499 per month'), ('700 for two months', '700 for two months'), ('Yearly subscription @3400', 'Yearly subscription @3400')], default='499 per month', max_length=20)),
                ('currency', models.CharField(choices=[('Rupees', 'Rupees'), ('Dollar', 'Dollar')], default='Rupees', max_length=20)),
                ('payment_method_types', models.CharField(choices=[('card', 'card'), ('paypal', 'paypal')], default='card', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='subscriptionpack',
            name='status',
            field=models.CharField(choices=[('expired', 'expired'), ('active', 'active')], default='expired', max_length=20),
        ),
    ]

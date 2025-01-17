# Generated by Django 5.0.4 on 2024-12-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('account_name', models.CharField(max_length=50, verbose_name='Account Name')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Total Amount')),
                ('number_of_accounts', models.PositiveIntegerField(default=0, verbose_name='Number of Accounts')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['-created_at'],
            },
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-13 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money_management', '0003_alter_transaction_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={},
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_remove_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='your_default_email@example.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='sdt',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

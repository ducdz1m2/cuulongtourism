# Generated by Django 4.2.7 on 2023-12-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_customer_email_customer_sdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='your_default_email@example.com', max_length=254),
        ),
    ]

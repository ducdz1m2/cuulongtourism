# Generated by Django 4.2.7 on 2023-12-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='chuongtrinhtour',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='soluoc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='trainghiem',
            field=models.TextField(blank=True),
        ),
    ]

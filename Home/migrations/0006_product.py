# Generated by Django 4.2.7 on 2023-12-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_food_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('khoihanh', models.CharField(max_length=50)),
                ('thoigian', models.IntegerField()),
                ('diadiem', models.CharField(max_length=100)),
                ('lichtrinh', models.TextField(blank=True)),
                ('gia', models.DecimalField(decimal_places=2, max_digits=15)),
                ('giachuasale', models.DecimalField(decimal_places=2, max_digits=15)),
                ('text_url', models.TextField(blank=True)),
            ],
        ),
    ]

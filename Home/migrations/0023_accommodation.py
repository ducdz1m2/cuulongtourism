# Generated by Django 4.2.7 on 2023-12-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_product_chuongtrinhtour_product_soluoc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gia', models.IntegerField(blank=True, default=0, null=True)),
                ('vitri', models.CharField(max_length=255)),
            ],
        ),
    ]
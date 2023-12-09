# Generated by Django 4.2.7 on 2023-12-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('mota', models.CharField(max_length=255)),
                ('text_url', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
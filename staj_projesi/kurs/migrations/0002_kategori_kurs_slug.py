# Generated by Django 4.2.5 on 2023-09-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='kurs',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]

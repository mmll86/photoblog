# Generated by Django 2.2.4 on 2019-08-14 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('image', models.ImageField(upload_to='images', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Slider_first',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('image', models.ImageField(upload_to='images', verbose_name='Картинка')),
            ],
        ),
    ]

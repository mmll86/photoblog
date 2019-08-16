# Generated by Django 2.2.4 on 2019-08-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photobloger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('text', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(height_field=400, upload_to='blog', verbose_name='Capture', width_field=400)),
            ],
        ),
    ]

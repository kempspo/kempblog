# Generated by Django 3.0.6 on 2020-05-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200530_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='background_image',
            field=models.ImageField(default='img/header.jpg', upload_to='backgrounds/2020/05/31'),
        ),
    ]

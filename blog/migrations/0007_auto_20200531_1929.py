# Generated by Django 3.0.6 on 2020-05-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='background_image',
            field=models.ImageField(upload_to='backgrounds/2020/05/31'),
        ),
    ]

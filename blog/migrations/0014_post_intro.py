# Generated by Django 3.0.6 on 2020-06-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200613_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(default='text', max_length=250),
            preserve_default=False,
        ),
    ]

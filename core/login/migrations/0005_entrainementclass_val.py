# Generated by Django 3.1.6 on 2021-04-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210410_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrainementclass',
            name='val',
            field=models.BooleanField(default=False),
        ),
    ]

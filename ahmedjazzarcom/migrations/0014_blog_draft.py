# Generated by Django 2.0.1 on 2018-01-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0013_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahmedjazzarcom', '0014_blog_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='header_color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]

# Generated by Django 2.0.4 on 2018-04-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='favourite',
            old_name='article',
            new_name='article_id',
        ),
        migrations.RenameField(
            model_name='favourite',
            old_name='user',
            new_name='user_id',
        ),
    ]

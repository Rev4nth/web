# Generated by Django 2.0.4 on 2018-04-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('about', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
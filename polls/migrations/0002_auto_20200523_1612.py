# Generated by Django 3.0.6 on 2020-05-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='choice',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='age',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]

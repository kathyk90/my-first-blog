# Generated by Django 3.0.6 on 2020-06-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_delete_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_code', models.CharField(max_length=200)),
                ('cod_2', models.CharField(max_length=200)),
                ('cod_3', models.CharField(max_length=200)),
            ],
        ),
    ]

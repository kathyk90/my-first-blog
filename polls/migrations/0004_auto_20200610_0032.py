# Generated by Django 3.0.6 on 2020-06-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='code',
            options={'ordering': ['-my_code']},
        ),
        migrations.RenameField(
            model_name='code',
            old_name='cod',
            new_name='cod_2',
        ),
        migrations.AddField(
            model_name='code',
            name='cod_3',
            field=models.CharField(default='default_cod', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='code',
            name='my_code',
            field=models.CharField(default='default_cod', max_length=200),
            preserve_default=False,
        ),
    ]

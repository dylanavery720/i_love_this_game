# Generated by Django 2.1.4 on 2018-12-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181204_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='apg',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='avatar',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='games',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='position',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='teamlogo',
            field=models.CharField(default='g', max_length=200),
            preserve_default=False,
        ),
    ]

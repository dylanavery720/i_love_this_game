# Generated by Django 2.1.4 on 2018-12-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181207_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='teamcolor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

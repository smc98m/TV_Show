# Generated by Django 2.2 on 2020-04-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0002_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='good'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Network',
        ),
    ]

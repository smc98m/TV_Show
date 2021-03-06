# Generated by Django 2.2 on 2020-04-14 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shows', models.ManyToManyField(related_name='networks', to='tv_app.Show')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_breakfast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='image',
            field=models.FileField(upload_to='todo/static/breakfasts'),
        ),
    ]

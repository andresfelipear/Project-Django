# Generated by Django 3.2.8 on 2021-10-30 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_breakfast_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCore', '0006_auto_20190604_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCore', '0010_auto_20190616_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='companyLoacation',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='companyName',
            field=models.CharField(max_length=128),
        ),
    ]
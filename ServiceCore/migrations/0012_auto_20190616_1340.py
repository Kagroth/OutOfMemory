# Generated by Django 2.2.1 on 2019-06-16 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCore', '0011_auto_20190616_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joboffer',
            old_name='companyLoacation',
            new_name='companyLocation',
        ),
    ]
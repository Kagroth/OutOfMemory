# Generated by Django 2.2.1 on 2019-06-04 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCore', '0004_auto_20190520_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('codeID', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=25)),
                ('codeField', models.CharField(max_length=2048)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cv',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cv', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='codeField',
            field=models.ManyToManyField(to='ServiceCore.Code'),
        ),
    ]
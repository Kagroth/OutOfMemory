# Generated by Django 2.1.4 on 2019-05-19 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCore', '0003_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ServiceCore.Post'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='ServiceCore.Comment'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='ratingValue',
            field=models.IntegerField(default=0),
        ),
    ]

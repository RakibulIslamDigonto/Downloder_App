# Generated by Django 4.0 on 2021-12-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_model',
            name='vidl_Body',
            field=models.CharField(max_length=600),
        ),
    ]

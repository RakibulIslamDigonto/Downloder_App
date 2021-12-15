# Generated by Django 4.0 on 2021-12-15 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createuser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_user', to='auth.user'),
            preserve_default=False,
        ),
    ]

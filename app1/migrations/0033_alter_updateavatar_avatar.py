# Generated by Django 5.0.3 on 2024-05-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_alter_updateavatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateavatar',
            name='avatar',
            field=models.ImageField(default='C:/Users/DELL/Downloads/GiasuWeb/app1/static/img/updateimg/Screenshot_2024-04-21_154314_7Laf2BW.png', upload_to='updateimg/'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-05-26 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0036_paymentrecord_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='updateinfo',
            name='date',
        ),
        migrations.AddField(
            model_name='updateinfo',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='updateimg/'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-06-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_paymentrecord_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecord',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

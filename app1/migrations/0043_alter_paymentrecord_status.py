# Generated by Django 5.0.3 on 2024-06-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_paymentrecord_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='status',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]

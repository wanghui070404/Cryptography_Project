# Generated by Django 5.0.3 on 2024-06-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0043_alter_paymentrecord_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='publickey',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='paymentrecord',
            name='signature',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-06-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_alter_paymentrecord_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='status',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]

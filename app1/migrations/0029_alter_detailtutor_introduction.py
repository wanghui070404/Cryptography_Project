# Generated by Django 5.0.3 on 2024-05-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_alter_detailtutor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtutor',
            name='Introduction',
            field=models.CharField(max_length=700),
        ),
    ]

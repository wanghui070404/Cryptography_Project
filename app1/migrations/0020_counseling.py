# Generated by Django 5.0.3 on 2024-04-27 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_detailtutor_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='COUNSELING',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
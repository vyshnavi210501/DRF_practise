# Generated by Django 5.1 on 2025-03-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20)),
                ('emp_name', models.CharField(max_length=100)),
                ('dessignation', models.CharField(max_length=50)),
            ],
        ),
    ]

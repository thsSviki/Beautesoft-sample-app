# Generated by Django 3.0.5 on 2020-04-09 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_app_req_outlet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_req',
            name='customer_area',
        ),
    ]

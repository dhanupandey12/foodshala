# Generated by Django 3.0.4 on 2020-05-18 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
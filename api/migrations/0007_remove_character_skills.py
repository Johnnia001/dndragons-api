# Generated by Django 3.2 on 2022-03-12 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220312_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='skills',
        ),
    ]

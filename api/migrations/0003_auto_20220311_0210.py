# Generated by Django 3.2 on 2022-03-11 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220309_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Option',
            new_name='Choice',
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-22 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='First_name',
            new_name='first_name',
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-27 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shiftrota', '0004_remove_shiftrotainfo_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shiftrotainfo',
            old_name='whichShift',
            new_name='shift',
        ),
    ]

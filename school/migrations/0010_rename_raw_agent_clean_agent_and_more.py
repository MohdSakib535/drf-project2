# Generated by Django 4.0.3 on 2024-01-22 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_raw_agent_raw_properties'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Raw_Agent',
            new_name='clean_Agent',
        ),
        migrations.RenameModel(
            old_name='Raw_properties',
            new_name='clean_properties',
        ),
        migrations.RenameModel(
            old_name='ListingCleaned_with_relation',
            new_name='properties',
        ),
    ]

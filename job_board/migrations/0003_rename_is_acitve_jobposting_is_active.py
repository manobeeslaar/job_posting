# Generated by Django 4.2.4 on 2023-08-16 12:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("job_board", "0002_jobposting_is_acitve"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobposting",
            old_name="is_acitve",
            new_name="is_active",
        ),
    ]
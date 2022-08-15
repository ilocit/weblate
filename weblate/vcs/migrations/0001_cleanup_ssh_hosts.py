# Generated by Django 3.2.7 on 2021-11-19 10:37

from django.db import migrations

from weblate.vcs.ssh import cleanup_host_keys


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(
            cleanup_host_keys, migrations.RunPython.noop, elidable=True
        )
    ]

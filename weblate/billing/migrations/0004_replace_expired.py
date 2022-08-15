# Generated by Django 3.1.2 on 2020-11-18 12:18

from django.db import migrations


def update_expired(apps, schema_editor):
    Billing = apps.get_model("billing", "Billing")
    Billing.objects.using(schema_editor.connection.alias).filter(state=2).update(
        state=1
    )


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0003_auto_20201118_1217"),
    ]

    operations = [
        migrations.RunPython(update_expired, migrations.RunPython.noop, elidable=True),
    ]

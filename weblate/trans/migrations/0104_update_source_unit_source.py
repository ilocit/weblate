# Generated by Django 3.1.1 on 2020-09-21 07:25

from django.db import migrations
from django.db.models import F


def update_source_unit(apps, schema_editor):
    Unit = apps.get_model("trans", "Unit")
    db_alias = schema_editor.connection.alias

    Unit.objects.using(db_alias).filter(
        translation__language=F("translation__component__source_language")
    ).update(source_unit_id=F("id"))


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0103_update_source_unit"),
    ]

    operations = [migrations.RunPython(update_source_unit, elidable=True)]

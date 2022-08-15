# Generated by Django 3.2.6 on 2021-09-30 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0012_migrate_kind"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="metric",
            unique_together={("date", "scope", "relation", "secondary", "kind")},
        ),
        migrations.RemoveField(
            model_name="metric",
            name="name",
        ),
    ]

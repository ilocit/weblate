# Generated by Django 3.0.7 on 2020-08-21 11:47

import django.db.models.deletion
from django.db import migrations, models

import weblate.lang.models


class Migration(migrations.Migration):

    dependencies = [
        ("lang", "0010_auto_20200627_0508"),
        ("glossary", "0003_fulltext"),
    ]

    operations = [
        migrations.AddField(
            model_name="glossary",
            name="source_language",
            field=models.ForeignKey(
                default=weblate.lang.models.get_default_lang,
                on_delete=django.db.models.deletion.CASCADE,
                to="lang.Language",
                verbose_name="Source language",
            ),
        ),
    ]

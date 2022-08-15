# Generated by Django 3.2.4 on 2021-07-21 06:47

from django.db import migrations

import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0137_alter_project_language_aliases"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="report_source_bugs",
            field=weblate.utils.fields.EmailField(
                blank=True,
                help_text="E-mail address for reports on errors in source strings. Leave empty for no e-mails.",
                max_length=190,
                verbose_name="Source string bug reporting address",
            ),
        ),
    ]

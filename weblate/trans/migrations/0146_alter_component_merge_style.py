# Generated by Django 4.0.1 on 2022-01-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0145_alter_change_action"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="merge_style",
            field=models.CharField(
                choices=[
                    ("merge", "Merge"),
                    ("rebase", "Rebase"),
                    ("merge_noff", "Merge without fast-forward"),
                ],
                default="rebase",
                help_text="Define whether Weblate should merge the upstream repository or rebase changes onto it.",
                max_length=10,
                verbose_name="Merge style",
            ),
        ),
    ]

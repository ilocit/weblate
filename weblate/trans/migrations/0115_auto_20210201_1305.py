# Generated by Django 3.1.4 on 2021-02-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0114_auto_20210129_1239"),
    ]

    operations = [
        migrations.AddField(
            model_name="component",
            name="glossary_color",
            field=models.CharField(
                choices=[
                    ("navy", "Navy"),
                    ("blue", "Blue"),
                    ("aqua", "Aqua"),
                    ("teal", "Teal"),
                    ("olive", "Olive"),
                    ("green", "Green"),
                    ("lime", "Lime"),
                    ("yellow", "Yellow"),
                    ("orange", "Orange"),
                    ("red", "Red"),
                    ("maroon", "Maroon"),
                    ("fuchsia", "Fuchsia"),
                    ("purple", "Purple"),
                    ("black", "Black"),
                    ("gray", "Gray"),
                    ("silver", "Silver"),
                ],
                default="silver",
                max_length=30,
                verbose_name="Glossary color",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="glossary_name",
            field=models.CharField(
                blank=True, max_length=60, verbose_name="Glossary name"
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="is_glossary",
            field=models.BooleanField(
                db_index=True, default=False, verbose_name="Use as a glossary"
            ),
        ),
    ]

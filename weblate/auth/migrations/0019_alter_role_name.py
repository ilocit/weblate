# Generated by Django 3.2.4 on 2021-09-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weblate_auth", "0018_fixup_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(max_length=200, unique=True, verbose_name="Name"),
        ),
    ]

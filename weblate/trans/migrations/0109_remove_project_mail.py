# Generated by Django 3.1.4 on 2021-01-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0108_move_mailing"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="mail",
        ),
    ]

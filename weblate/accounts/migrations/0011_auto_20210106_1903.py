# Generated by Django 3.1.3 on 2021-01-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_auto_20201213_1314"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auditlog",
            name="activity",
            field=models.CharField(
                choices=[
                    ("auth-connect", "auth-connect"),
                    ("auth-disconnect", "auth-disconnect"),
                    ("connect", "connect"),
                    ("email", "email"),
                    ("failed-auth", "failed-auth"),
                    ("full_name", "full_name"),
                    ("invited", "invited"),
                    ("locked", "locked"),
                    ("login", "login"),
                    ("login-new", "login-new"),
                    ("password", "password"),
                    ("register", "register"),
                    ("removed", "removed"),
                    ("reset", "reset"),
                    ("reset-request", "reset-request"),
                    ("sent-email", "sent-email"),
                    ("tos", "tos"),
                    ("trial", "trial"),
                    ("username", "username"),
                ],
                db_index=True,
                max_length=20,
            ),
        ),
    ]

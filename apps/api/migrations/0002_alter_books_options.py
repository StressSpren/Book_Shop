# Generated by Django 5.1.5 on 2025-02-09 22:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="books",
            options={"verbose_name_plural": "Books"},
        ),
    ]

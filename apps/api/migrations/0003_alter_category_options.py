# Generated by Django 5.1.6 on 2025-03-04 18:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_books_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]

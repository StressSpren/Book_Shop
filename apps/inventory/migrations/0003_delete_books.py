# Generated by Django 5.1.5 on 2025-02-09 22:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0002_alter_books_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Books",
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-26 07:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_rename_profile_article_author_and_more"),
        ("profile", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Profile",
            new_name="Author",
        ),
    ]

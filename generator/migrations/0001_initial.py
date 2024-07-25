# Generated by Django 5.2.dev20240620164851 on 2024-06-20 17:51

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SecurityRelease",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "releases",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=10), size=None
                    ),
                ),
                ("when", models.DateTimeField()),
                ("who", models.CharField(max_length=1024)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="SecurityIssue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cve_year_number", models.CharField(max_length=1024, unique=True)),
                (
                    "cve_type",
                    models.CharField(
                        choices=[
                            ("Buffer Overflow", "Buffer Overflow"),
                            (
                                "Cross Site Request Forgery (CSRF)",
                                "Cross Site Request Forgery (CSRF)",
                            ),
                            (
                                "Cross Site Scripting (XSS)",
                                "Cross Site Scripting (XSS)",
                            ),
                            ("Directory Traversal", "Directory Traversal"),
                            ("Incorrect Access Control", "Incorrect Access Control"),
                            ("Insecure Permissions", "Insecure Permissions"),
                            ("Integer Overflow", "Integer Overflow"),
                            (
                                "Missing SSL Certificate Validation",
                                "Missing SSL Certificate Validation",
                            ),
                            ("SQL Injection", "SQL Injection"),
                            ("XML External Entity (XXE)", "XML External Entity (XXE)"),
                            ("Other or Unknown", "Other or Unknown"),
                        ],
                        max_length=1024,
                    ),
                ),
                ("other_cve_type", models.CharField(default="", max_length=1024)),
                (
                    "severity",
                    models.CharField(
                        choices=[
                            ("low", "Low"),
                            ("moderate", "Moderate"),
                            ("high", "High"),
                        ],
                        default="low",
                    ),
                ),
                ("summary", models.CharField(max_length=1024)),
                ("description", models.TextField()),
                ("reporter", models.CharField(max_length=1024)),
                (
                    "release",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generator.securityrelease",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 6.0.dev20250310121938 on 2025-03-10 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("generator", "0023_remove_betarelease_feature_release_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="featurerelease",
            name="eol_release",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="generator.release",
            ),
        ),
        migrations.AddField(
            model_name="featurerelease",
            name="eom_release",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="generator.release",
            ),
        ),
        migrations.AddField(
            model_name="featurerelease",
            name="highlights",
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 2.1 on 2018-08-12 20:58

import colossus.apps.core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "city",
                "verbose_name_plural": "cities",
                "db_table": "colossus_cities",
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        max_length=2, unique=True, verbose_name="country code"
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="name")),
            ],
            options={
                "verbose_name": "country",
                "verbose_name_plural": "countries",
                "db_table": "colossus_countries",
            },
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.CharField(max_length=50, unique=True, verbose_name="key"),
                ),
                ("value", models.TextField(blank=True, verbose_name="value")),
            ],
            options={
                "verbose_name": "option",
                "verbose_name_plural": "options",
                "db_table": "colossus_options",
            },
        ),
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.CharField(
                        default=colossus.apps.core.models.default_token,
                        editable=False,
                        max_length=50,
                        unique=True,
                    ),
                ),
                ("description", models.CharField(db_index=True, max_length=30)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_used", models.DateTimeField(blank=True, null=True)),
                ("expires", models.IntegerField(default=7)),
                ("object_id", models.PositiveIntegerField(null=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
            options={
                "verbose_name": "token",
                "verbose_name_plural": "tokens",
                "db_table": "colossus_tokens",
            },
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cities",
                to="core.Country",
                verbose_name="country",
            ),
        ),
    ]

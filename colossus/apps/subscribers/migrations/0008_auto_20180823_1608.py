# Generated by Django 2.1 on 2018-08-23 13:08

from django.db import migrations, models, transaction
import django.db.models.deletion


def create_domains(apps, schema_editor):
    Domain = apps.get_model("subscribers", "Domain")
    Subscriber = apps.get_model("subscribers", "Subscriber")
    domain_cache = dict()
    with transaction.atomic():
        for subscriber in Subscriber.objects.all():
            email_name, domain_part = subscriber.email.rsplit("@", 1)
            domain_name = "@" + domain_part

            if domain_name not in domain_cache:
                domain_cache[domain_name], created = Domain.objects.get_or_create(
                    name=domain_name
                )

            subscriber.domain = domain_cache[domain_name]
            subscriber.save(update_fields=["domain"])


class Migration(migrations.Migration):
    dependencies = [
        ("subscribers", "0007_auto_20180823_1118"),
    ]

    operations = [
        migrations.CreateModel(
            name="Domain",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "domain",
                "verbose_name_plural": "domains",
                "db_table": "colossus_domains",
            },
        ),
        migrations.AddField(
            model_name="subscriber",
            name="domain",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="subscribers",
                to="subscribers.Domain",
                verbose_name="domain",
            ),
        ),
        migrations.RunPython(create_domains),
    ]
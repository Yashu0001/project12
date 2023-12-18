# Generated by Django 2.1 on 2018-08-23 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("subscribers", "0008_auto_20180823_1608"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscriber",
            name="domain",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="subscribers",
                to="subscribers.Domain",
                verbose_name="domain",
            ),
        ),
    ]

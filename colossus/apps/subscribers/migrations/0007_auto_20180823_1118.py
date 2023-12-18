# Generated by Django 2.1 on 2018-08-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscribers", "0006_auto_20180820_2016"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="activity_type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Subscribed"),
                    (2, "Unsubscribed"),
                    (3, "Was sent"),
                    (4, "Opened"),
                    (5, "Clicked"),
                    (6, "Imported"),
                    (7, "Cleaned"),
                ],
                verbose_name="type",
            ),
        ),
    ]
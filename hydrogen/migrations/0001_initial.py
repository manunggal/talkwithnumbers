# Generated by Django 4.2.8 on 2023-12-08 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CO2eEmissionsBenchmark",
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
                ("year", models.IntegerField(help_text="Year of the benchmark data")),
                (
                    "value",
                    models.FloatField(
                        help_text="Total CO2e emissions in megatonnes per year"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the CO2e emissions source",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        blank=True,
                        help_text="Additional information about the benchmark data",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ElectricityProductionBenchmark",
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
                ("year", models.IntegerField(help_text="Year of the benchmark data")),
                (
                    "value",
                    models.FloatField(
                        help_text="Total electricity production in Terra Watt-hours (TWh) per year"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the electricity production source",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        blank=True,
                        help_text="Additional information about the benchmark data",
                        null=True,
                    ),
                ),
            ],
        ),
    ]

from django.db import models

class ElectricityProductionBenchmark(models.Model):
    # The 'year' field represents the year of the benchmark data.
    year = models.IntegerField(help_text="Year of the benchmark data")
    
    # The 'value' field is the total electricity production for the year
    # stored in gigawatt-hours (GWh).
    value = models.FloatField(help_text="Total electricity production in Terra Watt-hours (TWh) per year")

    # The 'name' field is the name of the electricity production source.
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the electricity production source")

    # The remarks field is for any additional information about the benchmark data.
    remarks = models.TextField(blank=True, null=True, help_text="Additional information about the benchmark data")

    def __str__(self):
        # String representation of the ElectricityProductionBenchmark model
        return f"Electricity Production Benchmark for {self.year}"

class CO2eEmissionsBenchmark(models.Model):
    # The 'year' field represents the year of the benchmark data.
    year = models.IntegerField(help_text="Year of the benchmark data")
    
    # The 'value' field is the total CO2e emissions for the year
    # stored in megatonnes (MtCO2e).
    value = models.FloatField(help_text="Total CO2e emissions in megatonnes per year")

    # The 'name' field is the name of the CO2e emissions source.
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the CO2e emissions source")

    # The remarks field is for any additional information about the benchmark data.
    remarks = models.TextField(blank=True, null=True, help_text="Additional information about the benchmark data")

    def __str__(self):
        # String representation of the CO2eEmissionsBenchmark model
        return f"CO2e Emissions Benchmark for {self.year}"

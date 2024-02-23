import polars as pl
import numpy as np

# Speed and SFOC data
design_speed = 16 # knots
sfoc = 23 # ton/day

# small functions
def calc_duration_hours(df, design_speed):
    return df.with_columns((pl.col('distance') / design_speed).alias('duration_hours'))

def calc_duration_days(df):
    return df.with_columns((pl.col('duration_hours') / 24).alias('duration_days'))

def calc_fuel_consumption(df, sfoc):
    return df.with_columns((pl.col('duration_days')*sfoc).alias('fuel_consumption_ton'))


# Trayek t-10 data
t10_df = pl.DataFrame(
    {
        'port_depart': ['Tj Perak', 'TIdore', 'Morotai', 'Galela', 'Maba', 'Weda'],
        'port_arrive': ['Tidore', 'Morotai', 'Galela', 'Maba', 'Weda', 'Tj Perak'],
        'distance': [1216, 156, 72, 144, 139, 1213],
    }
)


# Calculate duration and fuel consumption
t10_df = (t10_df
          .pipe(calc_duration_hours, design_speed)
          .pipe(calc_duration_days)
          .pipe(calc_fuel_consumption, sfoc))

print(t10_df)

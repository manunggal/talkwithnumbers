import polars as pl
import numpy as np

#  referensi
#  https://ppid.dephub.go.id/fileupload/informasi-berkala/20230512143919.SK_Jaringan_Trayek_Tol_Laut_TA._2023.pdf

# Assumptions
design_speed = 16 # knots
sfoc = 23 # ton/day
total_annual_trips_numbers = 24

# small functions
def calc_duration_hours(df, design_speed):
    return df.with_columns((pl.col('distance') / design_speed).alias('voyage_duration_hours'))

def calc_voyage_duration_days(df):
    return df.with_columns((pl.col('voyage_duration_hours') / 24).alias('voyage_duration_days'))

def calc_fuel_consumption(df, sfoc):
    return df.with_columns((pl.col('voyage_duration_days')*sfoc).alias('fuel_consumption_ton'))

def calc_hours_to_days(df):
    return df.with_columns((pl.col('container_handling_duration_hours')/24).alias('container_handling_duration_days'))

def rounding_days(df):
    return df.with_columns((pl.col('total_duration_days') + 0.999999).cast(pl.Int32).alias('total_duration_days'))

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
          .pipe(calc_voyage_duration_days)
          .pipe(calc_fuel_consumption, sfoc))



# add dwelling time
t10_df = t10_df.with_columns(
    pl.Series(
        "container_handling_duration_hours", 
        [48, 24, 24, 12, 12, 48])
        ).pipe(calc_hours_to_days)

t10_df = t10_df.with_columns(
    (pl.col('voyage_duration_days') + pl.col('container_handling_duration_days')).alias('total_duration_days')
).pipe(rounding_days)
print(t10_df)

# resume
total_voyage_days = t10_df.select(pl.sum('voyage_duration_days'))
total_handling_days = t10_df.select(pl.sum('container_handling_duration_days'))
total_duration_days =  t10_df.select(pl.sum('total_duration_days'))

# print(f'voyage = {total_voyage_days}, handling = {total_handling_days}, total = {total_duration_days}')
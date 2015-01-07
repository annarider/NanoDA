import numpy
import pandas

def describe(subway_df):

    with_rain = pandas.Series(subway_df['rain'])
    print with_rain.value_counts()

    return subway_df['ENTRIESn_hourly'].describe()

if __name__ == '__main__':
    subway_df = pandas.read_csv('turnstile_weather_v2.csv')
    print describe(subway_df)


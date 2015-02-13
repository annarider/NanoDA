import numpy
import scipy.stats
import pandas


def calc_ander_subway(subway_df):

    with_rain = subway_df['ENTRIESn_hourly'][subway_df['rain'] == 1]
    without_rain = subway_df['ENTRIESn_hourly'][subway_df['rain'] == 0]

    anderson_rain = scipy.stats.anderson(subway_df['ENTRIESn_hourly'], dist='norm')
    anderson_norain = scipy.stats.anderson(without_rain)

    return anderson_rain, anderson_norain


if __name__ == '__main__':
    subway_df = pandas.read_csv('turnstile_weather_v2.csv')
    print calc_ander_subway(subway_df)
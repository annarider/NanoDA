import numpy
import scipy.stats
import pandas

def calc_shapwilk_subway(subway_df):

    with_rain = subway_df['ENTRIESn_hourly'][subway_df['rain'] == 1]
    without_rain = subway_df['ENTRIESn_hourly'][subway_df['rain'] == 0]

    # reference: http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.shapiro.html
    shapwilk_test = [scipy.stats.shapiro(with_rain), scipy.stats.shapiro(without_rain)]

    return shapwilk_test


if __name__ == '__main__':
    subway_df = pandas.read_csv('turnstile_weather_v2.csv')
    print calc_shapwilk_subway(subway_df)

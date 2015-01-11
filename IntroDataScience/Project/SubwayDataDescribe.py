import numpy
import pandas

def describe(subway_df):

    with_rain = pandas.Series(subway_df['rain'])
    print with_rain.value_counts()

    print "rain"
    print subway_df['rain'].describe()
    total_rain_records = numpy.sum(subway_df['rain'])
    print "total rain", total_rain_records

    print "mean, with rain", numpy.mean(subway_df['ENTRIESn_hourly'][subway_df['rain'] == 1])
    print "mean, with norain", numpy.mean(subway_df['ENTRIESn_hourly'][subway_df['rain'] == 0])

    return subway_df['ENTRIESn_hourly'].describe()

if __name__ == '__main__':
    subway_df = pandas.read_csv('turnstile_weather_v2.csv')
    print describe(subway_df)


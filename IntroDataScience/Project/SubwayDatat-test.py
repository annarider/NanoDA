import numpy
import scipy.stats
import pandas

def calc_ttest_subway(subway_df):

    with_rain = subway_df['ENTRIESn_hourly'][subway_df['rain'] == 1]
    without_rain = subway_df['ENTRIESn_hourly'][subway_df['rain'] == 0]

    ttest = scipy.stats.ttest_ind(with_rain, without_rain, equal_var=False)

    # print the mean of each sample dataset 
    print numpy.mean(with_rain)
    print numpy.mean(without_rain)

    print len(with_rain)
    print len(without_rain)

    if ttest[1] <= .05:
        return False, ttest
    else:
        return True, ttest


if __name__ == '__main__':
    subway_df = pandas.read_csv('turnstile_weather_v2.csv')
    print calc_ttest_subway(subway_df)


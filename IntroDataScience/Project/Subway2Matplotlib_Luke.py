import numpy as np
import pandas 
import matplotlib.pyplot as plt

def entries_histogram(subway_data_df):
    '''
    One visualization should contain two histograms: one of ENTRIESn_hourly for 
    rainy days and one of ENTRIESn_hourly for non-rainy days.
    You can combine the two histograms in a single plot or you can use 
    two separate plots.

    If you decide to use to two separate plots for the two histograms, 
    please ensure that the x-axis limits for both of the plots are identical. 
    It is much easier to compare the two in that case.
    For the histograms, you should have intervals representing the volume of 
    ridership (value of ENTRIESn_hourly) on the x-axis and the frequency of 
    occurrence on the y-axis. For example, you might have one interval 
    (along the x-axis) with values from 0 to 1000. The height of the bar for 
    this interval will then represent the number of records (rows in our data) 
    that have ENTRIESn_hourly that fall into this interval.
    Remember to increase the number of bins in the histogram 
    (by having larger number of bars). 
    The default bin width is not sufficient to capture the variability in the two samples.

    Remember to add appropriate titles and axes labels to your plots. 
    Also, please add a short description below each figure commenting on 
    the key insights depicted in the figure. 

    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms

    '''
    #All columns, but only rows that had rain
    no_rain_df = subway_data_df[subway_data_df['rain'] == 1]
    #import pdb; pdb.set_trace()
    #plt.figure()
    
    #Histogram of the entries column
    pandas.DataFrame.hist(no_rain_df, column = 'ENTRIESn_hourly', bins = 250)
    #print no_rain_df
    #pandas.DataFrame.hist(no_rain_df, bins = 250)
    #no_rain_df.show()

    return no_rain_df

# sample code
# P.figure()

# create a new data-set
# x = mu + sigma*P.randn(1000,3)

# n, bins, patches = P.hist(x, 10, normed=1, histtype='bar',
#                             color=['crimson', 'burlywood', 'chartreuse'],
#                             label=['Crimson', 'Burlywood', 'Chartreuse'])
# P.legend()

if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entries_histogram(subway_data_df)

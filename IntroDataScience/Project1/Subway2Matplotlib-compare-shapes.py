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
   
    # filtering the data to only take hourly entries with rain and without rain
    rain_df = subway_data_df['ENTRIESn_hourly'][subway_data_df['rain'] == 1]
    no_rain_df = subway_data_df['ENTRIESn_hourly'][subway_data_df['rain'] == 0]

    # create figure & axes for 2 subplots on same figure
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(14, 6))

    # setting the number of bins
    numbins = 250
    
    # creating histogram with visual cues, incl. colors & legends
    # use ax to plot the two subplots on the same figure
    no_rain_df.hist(bins = numbins, label = "No Rain", color='k', alpha = 0.5, grid = False, ax=ax0)
    rain_df.hist(bins = numbins, label = "Rain", color = "red", alpha = 0.75, grid = False, ax=ax1)
    
    # subway_data_df.hist([subway_data_df['ENTRIESn_hourly'], subway_data_df['rain']], bins = 50)

    # add axes labels
    ax0.set_xlabel("Hourly Entries")
    ax0.set_ylabel("Frequency")
    ax1.set_xlabel("Hourly Entries")
    ax1.set_ylabel("Frequency")

    # add titles to histograms
    ax0.set_title("Distribution of hourly entries without rain")
    ax1.set_title("Distribution of hourly entries with rain")

  
    plt.show()

    return no_rain_df

if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entries_histogram(subway_data_df)

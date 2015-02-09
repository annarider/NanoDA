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
    plt.figure()

    # filtering the data to only take hourly entries with rain and without rain
    rain_df = subway_data_df['ENTRIESn_hourly'][subway_data_df['rain'] == 1]
    no_rain_df = subway_data_df['ENTRIESn_hourly'][subway_data_df['rain'] == 0]

    # setting the number of bins
    binsize = 50
    
    # creating histogram with visual cues, incl. colors & legends
    no_rain_df.hist(bins = binsize, label = "No Rain", color='k', alpha = 0.5, grid = False)
    rain_df.hist(bins = binsize, label = "Rain", color = "red", alpha = 0.75, grid = False)
    

    # subway_data_df.hist([subway_data_df['ENTRIESn_hourly'], subway_data_df['rain']], bins = 50)

    # add axes labels
    plt.xlabel("Hourly Entries")
    plt.ylabel("Frequency")

    # add title to histogram
    plt.title("Distribution of hourly entries")

    # description to explain the histogram
    # description =   '''
    #                 vTart I love gummi bears cupcake                     
    #                 '''

    # add description to histogram - doesn't work!!!
    # plt.figtext(0, -3000, description)


    plt.legend()
    plt.show()

    return no_rain_df

# sample code from matplotlib's website -- use as guidelines
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

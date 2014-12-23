from pandas import *
from ggplot import *
import numpy 

def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    turnstile_df = pandas.read_csv(turnstile_weather)  
    minTemp = int(numpy.amin(turnstile_df['meantempi']))
    maxTemp = int(numpy.amax(turnstile_df['meantempi']))

    temps = []
    avgEntries = []

    for i in range(minTemp, maxTemp + 1):
        avgEntry = numpy.mean(turnstile_df['ENTRIESn_hourly'][turnstile_df['meantempi'] == i])
        temps.append(i)
        avgEntries.append(avgEntry)

    temp_entries_df = pandas.DataFrame({'temp': Series(temps), 'entries': (avgEntries)})

    # print temp_entries_df
    # plot = ""
    plot = ggplot(temp_entries_df, aes('temp', 'entries')) \
            + geom_point(color= 'red') + geom_line() + ggtitle('Entries by Avg. Temp.')
    # plot = ggplot(temp_entries_df, aes('temp', 'entries')) \
    #         + geom_bar(stat= 'identity') + ggtitle('Entries by Avg. Temp.')
 

    return plot

print plot_weather_data('../p3/turnstile_data_master_with_weather.csv')

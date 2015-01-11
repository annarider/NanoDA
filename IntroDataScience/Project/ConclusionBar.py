import numpy as np
import pandas 
import matplotlib.pyplot as plt

''' 
The goal of this code is to plot all the datetimes for one unit, and every rain value
i.e. 0 or 1. The idea is to calculate how many times it rained in NYC during the month
this data was collected. It is important for estimating the number of rain storms the
city had instead of relying on individual rain records that don't necessarily account
for continuous rain storms.
'''

def entriesBar(subway_data_df): 

    # takes only data from the 1st unit, R003, from the improved turnstile weather dataset
    # take a subset of the data that contains only datetime and rain columns        
    one_unit_data_df = subway_data_df['datetime'][subway_data_df['rain'][subway_data_df['UNIT'] == 'R003']]
    print one_unit_data_df

    # set the plot type to bar chart
    one_unit_data_df.plot(kind = "bar")

    # add title to histogram
    plt.title("Average hourly entries per day of week")

    # add axes labels
    plt.xlabel("Day of the week")
    plt.ylabel("Average Hourly Entries")

    # remove legend from plot
    legend = plt.legend()
    legend.remove()

    plt.show()

    return plt


if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entriesBar(subway_data_df)

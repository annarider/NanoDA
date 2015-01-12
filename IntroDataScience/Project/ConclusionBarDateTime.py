import numpy as np
import pandas 
import matplotlib.pyplot as plt

''' 
The goal of this code is to plot all the datetimes for one unit, and every rain value
i.e. 0 or 1. The idea is to calculate how many times it rained in NYC during the month
this data was collected. It is important for estimating the number of rain storms the
city had instead of relying on individual rain records that don't necessarily account
for continuous rain storms.

This chart uses datetime, so the multiple records per day haven't been aggregated. 
See subsequent code that calculates the rain per day, aggregating daily rain data together.
'''

def entriesBar(subway_data_df): 

    # takes only data from the 1st unit, R003, from the improved turnstile weather dataset
    # take a subset of the data that contains only datetime and rain columns        
    rain_1unit_series = pandas.Series(subway_data_df['rain'][subway_data_df['UNIT'] == 'R003'], name='Rain')

    datetime_series = pandas.Series(subway_data_df['datetime'][subway_data_df['UNIT'] == 'R003'], name='Datetime')

    one_unit_data_df = pandas.DataFrame({'Rain': rain_1unit_series})
    print one_unit_data_df

    # rotate the x ticks labels 90 degrees for readability
    plt.xticks(rotation=90)

    # set the plot type to bar chart
    one_unit_data_df.plot(kind = "bar")

    # add title to histogram
    plt.title("Distribution of rain for unit R003")

    # add axes labels
    plt.xlabel("Datetime")
    plt.ylabel("Rain or No Rain")


    plt.show()

    return plt


if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entriesBar(subway_data_df)

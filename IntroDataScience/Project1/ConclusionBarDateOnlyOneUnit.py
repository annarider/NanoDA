import numpy as np
import pandas 
import matplotlib.pyplot as plt

''' 
The goal of this code is to plot a sum of rain for all units. The code groups
the turnstile dataframe by date, and sums together all the rain data.  
The idea is to calculate how many times it rained in NYC during the month
this data was collected. Although the code could have observed only one unit,
I decided to sum all units together in case one station had rain and another did 
not at the same time on the same day.

This chart uses date only, so the multiple records per day have been aggregated. 
'''

def entriesBar(subway_data_df): 

    # takes only data from the 1st unit, R003, from the improved turnstile weather dataset
    # take a subset of the data that contains only date and rain columns 

    one_unit = subway_data_df[subway_data_df['UNIT'] == 'R003']       
    one_unit_data_df = one_unit.groupby('DATEn', as_index=False)['rain'].sum()

    # multiply by 4 to reflect time the samples were taken (6 times a day) 
    one_unit_data_df = one_unit_data_df * 4

    # set the plot type to bar chart
    one_unit_data_df.plot(kind = "bar")


    # rotate the x ticks labels 90 degrees for readability
    plt.xticks(rotation=90)

    # add title to histogram
    plt.title("Distribution of rain for unit R003 in May 2011")

    # add axes labels
    plt.xlabel("Day of Month")
    plt.ylabel("Number of hours of rain a day")


    plt.show()

    return plt


if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entriesBar(subway_data_df)


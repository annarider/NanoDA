import numpy as np
import pandas 
import matplotlib.pyplot as plt

def entriesBar(subway_data_df):
    ''' this method takes in a turnstile_weather dataframe and calls a process entries
    method to create a List to store all the days of the week as keys in a List
    and stores the average hourly entries per day as the values of the List. the method
    then draws the bar plot representing the average hourly entries per day for subway
    ridership data'''     
        
    daysOfTheWeekEntries = processEntriesList(subway_data_df)
    print daysOfTheWeekEntries

    # init the pyplot -- turns out this is unnecessary & only create an empty plot
    # plt.figure()

    # creating a pandas dataframe from the List to use for a matplotlib bar chart

    avgDailyEntries = pandas.DataFrame({'Average Hourly Entries': daysOfTheWeekEntries}, \
        index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # create list of colors for bar faces
    colors = ['b','g','r','c','y','m','k']
    # set the plot type to bar chart
    avgDailyEntries.plot(kind = "bar", color = colors)
    print avgDailyEntries

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


def processEntriesList(subway_data_df):
    ''' this method creates a List of 7 days in a week and calls the method that 
    calculates the average number of entries per day, then stores the average entries
    in the List to pass to the method to create the matplotlib bar chart '''  

    # init a List to store days of the week, which will be x-axis values in plot
    # 0 - 4 = Monday - Friday; 5, 6 = Saturday, Sunday
    avgEntriesDaily = []

    # calculate average entries per day of week & add to List
    for i in range(0,7):
        avgEntriesDaily.append(calculateAvgEntries(subway_data_df, i))

    return avgEntriesDaily



def calculateAvgEntries(subway_data_df, day):
    ''' this method calculates the average hourly entries based on each day of the week
    and returns a float representing the number of hourly entries for a particular day '''

    # filtering the data to only take hourly entries based on day of week
    allENTRIESn_hourly = subway_data_df['ENTRIESn_hourly'][subway_data_df['day_week'] == day]
    return np.mean(allENTRIESn_hourly)

if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entriesBar(subway_data_df)

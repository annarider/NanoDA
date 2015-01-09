import numpy as np
import pandas 
import matplotlib.pyplot as plt

def entriesBar(subway_data_df):
    ''' this method takes in a turnstile_weather dataframe and calls a process entries
    method to create a dict to store all the days of the week as keys in a dict
    and stores the average hourly entries per day as the values of the dict. the method
    then draws the bar plot representing the average hourly entries per day for subway
    ridership data'''     
        
    daysOfTheWeekEntries = processEntriesDict(subway_data_df)

    print daysOfTheWeekEntries

    # inti the pyplot
    plt.figure()

    # creating a pandas dataframe from the dict to use for a matplotlib bar chart

    # avgDailyEntries = pandas.DataFrame(daysOfTheWeekEntries), index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # avgDailyEntries.plot(kind = "bar")

    # add title to histogram
    plt.title("Average hourly entries per day of week")

    # add axes labels
    plt.xlabel("Day of the week")
    plt.ylabel("Average Hourly Entries")

    plt.show()

    print avgDailyEntries
        # setting the number of bins
    # binsize = 50
    
    # creating histogram with visual cues, incl. colors & legends

    # subway_data_df.hist([subway_data_df['ENTRIESn_hourly'], subway_data_df['rain']], bins = 50)






    # plt.legend()
    # plt.show()

    # return no_rain_df


def processEntriesDict(subway_data_df):
    ''' this method creates a dict of 7 days in a week and calls the method that 
    calculates the average number of entries per day, then stores the average entries
    in the dict to pass to the method to create the matplotlib bar chart '''  

    # init a dict to store days of the week, which will be x-axis values in plot
    # 0 - 4 = Monday - Friday; 5, 6 = Saturday, Sunday
    daysOfTheWeek = dict.fromkeys([0,1,2,3,4,5,6])

    # calculate average entries per day of week & add to dict
    for i in range(0,7):
        daysOfTheWeek[i] = calculateAvgEntries(subway_data_df, i)


    return daysOfTheWeek



def calculateAvgEntries(subway_data_df, day):
    ''' this method calculates the average hourly entries based on each day of the week
    and returns a float representing the number of hourly entries for a particular day '''

    # filtering the data to only take hourly entries based on day of week
    allENTRIESn_hourly = subway_data_df['ENTRIESn_hourly'][subway_data_df['day_week'] == day]
    return np.mean(allENTRIESn_hourly)

if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    entriesBar(subway_data_df)

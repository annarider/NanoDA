import numpy as np
import pandas 
import matplotlib.pyplot as plt

def rain_entries_scatter(subway_data_df):
   
    # filtering the data to only take the precipitation at time & location
    precipi = subway_data_df['precipi']
    norm_precipi = normalize(precipi) 
    # filtering for hourly entries
    entries = subway_data_df['ENTRIESn_hourly']

    # create scatter plot 
    plt.scatter(norm_precipi, entries)
    
    # determine best fit line to visually see trend
    slope, intercept = np.polyfit(norm_precipi, entries, 1)
    print 'slope = ', slope
    print 'intercept = ', intercept

    yfit = slope * norm_precipi + intercept
    # calculates the error
    error = entries - yfit

    # plot line of best fit
    best_fit = plt.plot(norm_precipi, yfit, 'r', label='linear fit')

    # add axes labels
    plt.xlabel("Precipitation (in)")
    plt.ylabel("Hourly Entries")
    # add legend
    plt.legend([slope], title='slope')

    # add titles to histograms
    plt.title("Hourly entries based on precipitation distribution")
      
    plt.show()

    return plt

def normalize(array):
    """
    Normalize the features in the data set.
    """
    array_normalized = (array-array.mean())/array.std()

    return array_normalized

if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    rain_entries_scatter(subway_data_df)

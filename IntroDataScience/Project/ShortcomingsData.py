import pandas 
import numpy as np 

'''
This code is for exploring the turnstile subway data to draw conclusions 
about its shortcomings.
For answer 5 in the 2nd half of the final Project.
'''

def subway_descrip(subway_data_df):

    print "Datetime column:"
    print subway_data_df['datetime']


if __name__ == '__main__':
    subway_data_df = pandas.read_csv('turnstile_weather_v2.csv')
    subway_descrip(subway_data_df)

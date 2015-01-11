import numpy as np
import pandas
import scipy
import statsmodels.api as sm

'''
Fri, Jan 9, 2015
ALi
This code is built to help answer the question of whether more people ride the subway
when it is raining.
The goal of running linear regression is to find the coefficients of theta to figure out
how strong of a relationship rain has to hourly entries. 

Features = rain, and 1.0 (constant to off set any biases)
Labels = ENTRIESn_hourly 
'''

def predictions(subway_df):
    # features: create a dataframe with all rain data rows (x values)
    features_df = pandas.DataFrame({'rain': subway_df['rain']})

    # labels: create a dataframe containing all hourly entries (Observations) (y values)
    labels_df = subway_df['ENTRIESn_hourly']

    # add constant to features to off set any bias
    features_df = sm.add_constant(features_df)
    print features_df

    # create OLS model
    model = sm.OLS(labels_df, features_df)

    # fit model points
    results = model.fit()
    print results

    print "params"
    print results.params

    print "summary"
    print results.summary()

    # run predictions 
    prediction = results.predict(features_df)
    
    return prediction

if __name__ == '__main__':
    subway_df = pandas.read_csv('turnstile_weather_v2.csv')
    print predictions(subway_df)

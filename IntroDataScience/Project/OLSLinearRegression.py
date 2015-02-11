import numpy as np
import pandas
import scipy
import statsmodels.api as sm

"""
In this optional exercise, you should complete the function called 
predictions(turnstile_weather). This function takes in our pandas 
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.  

In exercise 3.5 we used Gradient Descent in order to compute the coefficients
theta used for the ridership prediction. Here you should attempt to implement 
another way of computing the coeffcients theta. You may also try using a reference implementation such as: 
http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.OLS.html

One of the advantages of the statsmodels implementation is that it gives you
easy access to the values of the coefficients theta. This can help you infer relationships 
between variables in the dataset.

You may also experiment with polynomial terms as part of the input variables.  

The following links might be useful: 
http://en.wikipedia.org/wiki/Ordinary_least_squares
http://en.wikipedia.org/w/index.php?title=Linear_least_squares_(mathematics)
http://en.wikipedia.org/wiki/Polynomial_regression

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent computed in Exercise 3.5?

You can look at the information contained in the turnstile_weather dataframe below:
https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~10%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting 
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""

def predictions(weather_turnstile):


    turnstile_df = weather_turnstile
    # print prediction

    # print prediction['hour']
    features_df = pandas.DataFrame({'hour': turnstile_df['hour'], 
                                    # 'rain': turnstile_df['rain'],
                                    'tempi': turnstile_df['tempi'],
                                    'meantempi': turnstile_df['meantempi'],
                                    'wspdi': turnstile_df['wspdi'],
                                    'meanwspdi': turnstile_df['meanwspdi'],
                                    'precipi': turnstile_df['precipi']})
    label = turnstile_df['ENTRIESn_hourly']

    # Adds y-intercept to model
    features_df = sm.add_constant(features_df)

    # add dummy variables of turnstile units to features
    dummy_units = pandas.get_dummies(turnstile_df['UNIT'], prefix='unit')
    # add dummy variables of rain to features (because rain is categorical)
    dummy_rain = pandas.get_dummies(turnstile_df['rain'], prefix='rain')

    features_df = features_df.join([dummy_rain, dummy_units])

    model = sm.OLS(label,features_df)
    # print model
    results = model.fit()
    # print results
    # print results.params
    # prediction = sm.OLS.predict(model,features_df)
    # print features_df
    # print results.predict(features_df)
    prediction = results.predict(features_df)
    return prediction

def compute_r_squared(label, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    sum_of_data_minus_predictions = np.sum(np.square(label - predictions))
    sum_of_predictions_minus_mean = np.sum(np.square(label - np.mean(label)))
    r_squared = 1 - (sum_of_data_minus_predictions / sum_of_predictions_minus_mean)

    return r_squared

def imp():
    turnstile_df = pandas.read_csv('turnstile_weather_v2.csv')
    return turnstile_df

if __name__ == '__main__':
    data = imp()
    prediction = predictions(data)
    label = data['ENTRIESn_hourly']
    # print "data: \n",data
    # print "pred: \n",prediction
    # print "lbl: \n",label
    
    print compute_r_squared(label,prediction)

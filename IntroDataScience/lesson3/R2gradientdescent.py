import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    sum_of_data_minus_predictions = np.sum(np.square(data - predictions))
    sum_of_predictions_minus_mean = np.sum(np.square(data - np.mean(data)))
    r_squared = 1 - (sum_of_data_minus_predictions / sum_of_predictions_minus_mean)

    return r_squared
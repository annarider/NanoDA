#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    
    # calculate threshold of 90%    
    residual_errors = net_worths - predictions 
    residual_errors_square = np.square(residual_errors)
    residual_errors_square.sort(axis = 0)
#    print residual_errors_square
    
    percentile_90_index = int(len(residual_errors_square) * .9)
    percentile_90_threshold = residual_errors_square[percentile_90_index - 1][0]
#    print "threshold", percentile_90_threshold
    
    cleaned_data_all = zip(ages[:, 0].tolist(), net_worths[:, 0].tolist(), residual_errors[:, 0].tolist())
    
#    count = 0
    
    for e in cleaned_data_all: 
        (age, net_worth, error) = e
        if np.square(error) <= percentile_90_threshold: 
#            print error, percentile_90_threshold
            cleaned_data.append(e)
#            count += 1
#    print count
    return cleaned_data

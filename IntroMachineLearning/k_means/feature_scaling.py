# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:24:37 2015

@author: horsepower
"""

""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    min_val = min(arr)
    max_val = max(arr)
    scaled_feature_list = []
    
    # test if min and max values are same   
    if max_val != min_val:
        for value in arr: 
            scaled_feature = float((value - min_val)) / (max_val - min_val)
            scaled_feature_list.append(scaled_feature)
    else: 
        return "Error: min and max are the same value"
    
    # return scaled feature list
    return scaled_feature_list

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)


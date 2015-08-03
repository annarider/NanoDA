#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["poi", "total_payments", "shared_receipt_with_poi"]


# remove TOTAL outlier
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

outlier_salary = 0
### your code below

for point in data:
    color = 'r' if point[0] == 1 else 'c'
    f1 = point[1]
    f2 = point[2]
    plt.scatter( f1, f2, color = color)
    
    

    # find outlier person    
    if f1 > 80000000:
        print features[1],":", f1, features[2], ":", f1
        outlier_salary = f1

# Find outlier in data_dict
for key in data_dict: 
#    print key
    if data_dict[key]['salary'] == outlier_salary:
        print key, outlier_salary

# find 4 outliers in cleaner dataset
for key in data: 
    f1 = key[1]
    if f1 > 800000:
        for p in data_dict:
            if data_dict[p][features[1]] == f1:
                print p

plt.xlabel(features[1])
plt.ylabel(features[2])
plt.legend()
plt.show()
plt.savefig("outliers.pdf")



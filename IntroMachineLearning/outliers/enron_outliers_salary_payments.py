#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["poi", "salary", "total_payments"]


# remove TOTAL outlier
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

outlier_salary = 0
### your code below

for point in data:
    color = 'y' if point[0] == 1 else 'c'
    salary = point[1]
    total_payments = point[2]
    plt.scatter( salary, total_payments, color = color)
    
    

    # find outlier person    
    if salary > 800000:
        print "salary:", salary, "total_payments:", total_payments
        outlier_salary = salary

# Find outlier in data_dict
for key in data_dict: 
#    print key
    if data_dict[key]['salary'] == outlier_salary:
        print key, outlier_salary

# find 4 outliers in cleaner dataset
for key in data: 
    salary = key[1]
    if salary > 800000:
        for p in data_dict:
            if data_dict[p]['salary'] == salary:
                print p

plt.xlabel("salary")
plt.ylabel("total_payments")
plt.legend()
plt.show()
plt.savefig("outliers.pdf")



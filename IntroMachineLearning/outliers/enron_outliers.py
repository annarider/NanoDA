#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

# remove TOTAL outlier
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

outlier_salary = 0
### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

    # find outlier person    
    if salary > 2500000:
        print "salary:", salary, "bonus:", bonus
        outlier_salary = salary

# Find biggest outlier in data_dict
for key in data_dict: 
#    print key
    if data_dict[key]['salary'] == outlier_salary:
        print key, outlier_salary

# find 4 outliers in cleaner dataset
for key in data: 
    salary = key[0]
    if salary > 600000:
        for p in data_dict:
            if data_dict[p]['salary'] == salary:
                print p

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
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

for key in data_dict: 
#    print key 
#    break
    if data_dict[key]['salary'] == outlier_salary:
        print key, outlier_salary


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



#!/usr/bin/python

import sys
import pickle
import json
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester_plot import test_classifier, dump_classifier_and_data
from selectkbest_analysis import analyze_feature_selection

#EMAIL_SUSPICIOUS_RATIO = "email_suspicious_ratio.pkl"
EMAIL_SUSPICIOUS_RATIO_JSON = "email_suspicious_ratio.json"

NEW_FEATURE = "suspicious_email_ratio"

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'total_payments', 'bonus', 'restricted_stock_deferred', 'director_fees'] #, NEW_FEATURE]

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

#print "num of data points", len(data_dict)


### Task 2: Remove outliers
### Task 3: Create new feature(s)
#with open(EMAIL_SUSPICIOUS_RATIO, 'r') as esr:
#    email_suspicious_total_ratio = pickle.load(esr)
with open(EMAIL_SUSPICIOUS_RATIO_JSON, 'r') as esrj:
    email_suspicious_total_ratio = json.load(esrj)

my_dataset = data_dict
### Store to my_dataset for easy export below.
for person in my_dataset:
    email = my_dataset[person]['email_address']
    my_dataset[person][NEW_FEATURE] = email_suspicious_total_ratio[email]
        
#analyze_feature_selection(my_dataset)

features_list_best = ['poi', 'total_stock_value', 'exercised_stock_options', 'expenses', 'salary']
data = featureFormat(my_dataset, features_list_best, sort_keys = True)
labels, features = targetFeatureSplit(data)
        
### Task 4: Try a variety of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()    # Provided to give you a starting point. Try a varity of classifiers.
        
#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier(n_neighbors = 10)

#from sklearn.svm import SVC
#clf = SVC(C = 10.0, kernel="rbf", degree=4)

from sklearn import tree
clf = tree.DecisionTreeClassifier()


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.
### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

from sklearn import grid_search
from sklearn.metrics import make_scorer, recall_score
recall_scorer = make_scorer(recall_score, greater_is_better=True) 

parameters = {'min_samples_split': [2, 5, 10],
                      'min_samples_leaf': [1, 2],
                      'max_depth': [None, 1],
                      'splitter' : ['best', 'random'],
                      'criterion': ['gini', 'entropy'],
                      'random_state': [42]
}
#
clf_grid_search = grid_search.GridSearchCV(clf, parameters, scoring=recall_scorer)

#clf = tree.DecisionTreeClassifier(compute_importances=None, criterion='entropy',
#            max_depth=None, max_features=10, min_density=None,
#            min_samples_leaf=1, min_samples_split=1, random_state=None,
#            splitter='best')
#test_classifier(clf, my_dataset, features_list_best)
test_classifier(clf_grid_search, my_dataset, features_list_best)
           
### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

dump_classifier_and_data(clf, my_dataset, features_list)
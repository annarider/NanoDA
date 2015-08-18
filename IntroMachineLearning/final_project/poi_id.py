#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

EMAIL_SUSPICIOUS_RATIO = "email_suspicious_ratio.pkl"
NEW_FEATURE = "suspicious_email_ratio"

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
#features_list = ['poi', 'salary', 'total_payments']
features_list = ['poi', 'total_payments', 'bonus', 'restricted_stock_deferred', 'director_fees', NEW_FEATURE]

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

#print "num of data points", len(data_dict)


### Task 2: Remove outliers
### Task 3: Create new feature(s)
with open(EMAIL_SUSPICIOUS_RATIO, 'r') as esr:
    email_suspicious_total_ratio = pickle.load(esr)

my_dataset = data_dict
### Store to my_dataset for easy export below.
for person in my_dataset:
    email = my_dataset[person]['email_address']
    my_dataset[person][NEW_FEATURE] = email_suspicious_total_ratio[email]
        
        
 

### Extract features and labels from dataset for local testing
#features_list_kbest = ['poi', 'salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees','to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']  # You will need to use more features
data = featureFormat(my_dataset, features_list, sort_keys = True)
#data = featureFormat(my_dataset, features_list_kbest, sort_keys = True)
labels, features = targetFeatureSplit(data)


### Run SelectKBest for feature selection
#from sklearn.feature_selection import SelectKBest, f_regression
#from sklearn import cross_validation
#
#features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
#	features, labels, test_size = 0.3, random_state = 42)
#
#kbest = SelectKBest(f_regression, k = 8)
#find_kbest_features = kbest.fit(features_train, labels_train)
#kbest_features_transformed = kbest.fit_transform(features_train, labels_train)
#print kbest.get_support()
#print find_kbest_features.scores_
#print find_kbest_features.pvalues_

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()    # Provided to give you a starting point. Try a varity of classifiers.

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion='gini', min_samples_split = 2, 
                                  min_samples_leaf=3, random_state=27)

#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier(n_neighbors = 10)

#from sklearn.svm import SVC
#clf = SVC(C = 10.0, kernel="rbf", degree=4)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.
### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

#classProbs = clf.predict_proba(featureMatrix)

#test_classifier(clf, my_dataset, features_list)
test_classifier(clf, my_dataset, features_list)

### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

dump_classifier_and_data(clf, my_dataset, features_list)
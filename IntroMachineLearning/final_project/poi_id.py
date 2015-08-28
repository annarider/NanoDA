#!/usr/bin/python

import sys
import pickle
import json
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester_plot import test_classifier, dump_classifier_and_data

#EMAIL_SUSPICIOUS_RATIO = "email_suspicious_ratio.pkl"
EMAIL_SUSPICIOUS_RATIO_JSON = "email_suspicious_ratio.json"

NEW_FEATURE = "suspicious_email_ratio"

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
#features_list = ['poi', 'salary', 'total_payments']
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
        
        
### Feature Selection, with learning curve to avoid overfitting
features_list_kbest = ['poi', 'salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees', 'to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']
    #['poi', 'salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees','to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']  # You will need to use more features

# plot scatterplot to see SelectKBest score v. precision & recall 
import matplotlib.pyplot as plt
precision_train_scores = []
precision_test_scores = []
recall_train_scores = []
recall_test_scores = []
kvalues = []

for i in range(1,len(features_list_kbest)):
        
    ### Extract features and labels from dataset for local testing
    #data = featureFormat(my_dataset, features_list, sort_keys = True)
    data = featureFormat(my_dataset, features_list_kbest, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    
    
    ### Run SelectKBest for feature selection
    from sklearn.feature_selection import SelectKBest, f_regression
    from sklearn import cross_validation
    
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    	features, labels, test_size = 0.3, random_state = 42)
    
    kbest = SelectKBest(f_regression, k = i)
    find_kbest_features = kbest.fit(features_train, labels_train)
    kbest_features_transformed = kbest.fit_transform(features_train, labels_train)
    print kbest.get_support()
    kvalues.append(i)
    print find_kbest_features.scores_
    print find_kbest_features.pvalues_
    #get the names of the top-scoring features
    score_featureName = zip(find_kbest_features.scores_,features_list_kbest[1:])
    score_featureName.sort()
    kbestFeatureNames = [n for (s,n) in score_featureName[:i]]
    print i,"best:",kbestFeatureNames
    #add in "poi"
    kbestFeatureNames = [features_list_kbest[0]]+kbestFeatureNames
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
    
    
    #test_classifier(clf, my_dataset, features_list)
    precision_train, recall_train, precision_test, recall_test = test_classifier(clf, my_dataset, kbestFeatureNames)

    precision_train_scores.append(precision_train)
    precision_test_scores.append(precision_test)
    recall_train_scores.append(recall_train)
    recall_test_scores.append(recall_test)

plt.figure()
plt.plot(kvalues, precision_train_scores, "-", label="training precision")
plt.plot(kvalues, precision_test_scores, "-", label="test precision")
plt.plot(kvalues, recall_train_scores, "-", label="training recall")
plt.plot(kvalues, recall_test_scores, "-", label="test recall")
plt.xlabel("k-value")
plt.ylabel("precision and recall scores")
plt.legend()
plt.show()
plt.savefig("kvalue_precision_recall.pdf")
   
### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

dump_classifier_and_data(clf, my_dataset, features_list)
#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess_percentile_change import preprocess
#from email_preprocess import preprocess
from sklearn import tree
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
clf_min_samples_split_40 = tree.DecisionTreeClassifier(min_samples_split = 40)

t0 = time()
clf_min_samples_split_40.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred_min_samples_split_40 = clf_min_samples_split_40.predict(features_test)
print "testing time:", round(time()-t1, 3), "s"


acc_min_samples_split_40 = accuracy_score(pred_min_samples_split_40, labels_test)
print "accuracy: ", acc_min_samples_split_40

print "number of features: ", len(features_train[0])


#########################################################

'''
Results

with Select Percentile = 10
training time: 98.657 s
testing time: 0.036 s
accuracy 0.977815699659
number of features: 3785

with Select Percentile = 1
training time: 5.699 s
testing time: 0.002 s
accuracy:  0.966439135381
number of features:  379
'''

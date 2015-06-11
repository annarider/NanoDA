#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


def identify_authors():

#########################################################
### create classifier
    clf = GaussianNB()

    ### timing to train algorithm
    t0 = time()
    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    ### print time taken to  train -- 3.33 s
    print "training time:", round(time()-t0, 3), "s"
    
    ### timing to test algorithm
    t1 = time()
    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    ### print time taken to test -- 0.893 s
    print "testing time:", round(time()-t1, 3), "s"

    ### calc accuracy
    accuracy = clf.score(features_test, labels_test)
    return accuracy

#########################################################

if __name__ == '__main__':
    print identify_authors()


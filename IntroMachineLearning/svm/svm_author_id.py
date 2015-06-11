#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################

clf = SVC(kernel="rbf")

# reduce size of training set to speed up svm 
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
### timing to train algorithm
t0 = time()
clf.fit(features_train, labels_train)
### print time taken to  train:
# full dataset linear 199.766 s / 1% linear kernel 0.114 s / rbf 0.191 s
print "training time:", round(time()-t0, 3), "s"

### timing to test algorithm
t1 = time()
pred = clf.predict(features_test)
### print time taken to test:
# full dataset linear 19.506 s / 1% linear kernel 1.368 s / rbf 1.629 s
print "testing time:", round(time()-t1, 3), "s"

# predict accuracy:
# full dataset linear 0.984072810011 / 1% linear kernel 0.884527872582 / rbf 0.616040955631
acc = accuracy_score(pred, labels_test)
print acc



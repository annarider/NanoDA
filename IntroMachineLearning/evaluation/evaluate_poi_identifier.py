#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

### split features & labels into training and test sets
from sklearn import cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
	features, labels, test_size = 0.3, random_state = 42)
	

### create not overfitted decision tree classifier
from sklearn import tree
from sklearn.metrics import accuracy_score


clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

prediction = clf.predict(features_test)

accuracy = accuracy_score(prediction, labels_test)


print accuracy

print prediction

# How many POIs are predicted for the test set for your POI identifier?
count = 0
for e in prediction:
	if e == 1:
		count += 1
print "num POIs in test set:", count 
print "num of ppl in test set:", len(prediction)

count2 = 0
for e in zip(labels_test, prediction):
	if e[0] == e[1] and e[0] == 1.0:
		count2 += 1
print count2


from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

precision = precision_score(labels_test, prediction)
print "precision:", precision

recall = recall_score(labels_test, prediction)
print "recall:", recall

#recall = TP / (TP + FN)
#precision = TP / (TP + FP)
#(Where TP = True Positive, TN = True Negative, FP = False Positive, FN = False Negative).


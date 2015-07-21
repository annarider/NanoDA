#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

### create overfit decision tree classifier
#from sklearn import tree
#from sklearn.metrics import accuracy_score
#
#
#clf = tree.DecisionTreeClassifier()
#clf.fit(features, labels)
#
#prediction = clf.predict(features)
#
#accuracy = accuracy_score(prediction, labels)
#

#print accuracy

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

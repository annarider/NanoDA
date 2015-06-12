from sklearn import tree

def classify(features_train, labels_train):
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)
    
    
    return clf
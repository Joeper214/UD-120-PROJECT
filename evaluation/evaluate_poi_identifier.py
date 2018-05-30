#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
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
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import cross_validation

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)
print clf.score(features, labels)

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)
pred = clf.predict(features_test)

sum(pred)
print len([e for e in labels_test if e == 1.0])

print len(pred)

# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print (1.0 - 5.0/29)

from sklearn.metrics import *

print precision_score(labels_test, pred)
print recall_score(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]


# What's the precision of this classifier?
print precision_score(true_labels, predictions)

# What's the recall of this classifier?
print recall_score(true_labels, predictions)

cm = confusion_matrix(true_labels, predictions)

print cm, '\n'
print '{0} True positives'.format(cm[1][1])
print '{0} True negatives'.format(cm[0][0])
print '{0} False positives'.format(cm[0][1])
print '{0} False negatives'.format(cm[1][0])
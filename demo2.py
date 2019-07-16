# CHALLENGE - create 3 more classifiers...
from sklearn import tree
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score # to show the accuracy percent
import numpy as np# to do calculation

clf_tree = tree.DecisionTreeClassifier()
clf_svm = SVC()
clf_perceptron = Perceptron()
clf_KNN = KNeighborsClassifier()

## [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


#train the data and test predict accarcy
clf_tree = clf_tree.fit(X,Y)
clf_svm = clf_svm.fit(X,Y)
clf_perceptron = clf_perceptron.fit(X,Y)
clf_KNN = clf_KNN.fit(X,Y)

prediction1 = clf_tree.predict(X)
acc_tree = accuracy_score(Y,prediction1)#test the relation -1 - 1
prediction2 = clf_svm.predict(X)
acc_tree2 = accuracy_score(Y,prediction2)#test the relation -1 - 1
prediction3 = clf_perceptron.predict(X)
acc_tree3 = accuracy_score(Y,prediction3)#test the relation -1 - 1
prediction4 = clf_KNN.predict(X)
acc_tree4 = accuracy_score(Y,prediction4)#test the relation -1 - 1

# The best classifier from svm, per, KNN
print('Accuracy for DecisionTree: {}'.format(acc_tree))
print('Accuracy for SVM: {}'.format(acc_tree2))
print('Accuracy for Perception: {}'.format(acc_tree3))
print('Accuracy for KNN: {}'.format(acc_tree4))

index = np.argmax([acc_tree,acc_tree2,acc_tree3,acc_tree4])
classifiers ={0:'tree',1:'SVM',2:'Perceptron',3:'KNN'}
print('BEST gender classifier is {}'.format(classifiers[index]))


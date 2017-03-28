# Decision Tree Classifier
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from CommonModel import *

# load the iris datasets
dataset = datasets.load_iris()
test_feature = [[5.2, 3.4, 1.3, 0.3]]

# my_model = CommonModel(DecisionTreeClassifier(), dataset)
# my_model = CommonModel(LogisticRegression(), dataset)
# my_model = CommonModel(BernoulliNB(), dataset)
# my_model = CommonModel(KNeighborsClassifier(), dataset)
my_model = CommonModel(svm.SVC(kernel="linear"), dataset)
#my_model = CommonModel(RandomForestClassifier(n_estimators=10), dataset)

my_model.train(dataset.data, dataset.target, test_size=0.4)

print my_model.getScore()

# plt.scatter(dataset.data,dataset.target,edgecolors="black")

print my_model.predict(test_feature)
from sklearn import svm
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

DECISION_TREE = DecisionTreeClassifier()
LOGISTIC_REGRESSION = LogisticRegression()
NAIVE_BAYS = BernoulliNB()
K_N_N = KNeighborsClassifier()
SUPPORT_VECTOR = svm.SVC(kernel="linear")
RANDOM_FOREST = RandomForestClassifier(n_estimators=10)

from sklearn import svm
from sklearn.ensemble.forest import RandomForestClassifier, ExtraTreesClassifier
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.ensemble.weight_boosting import AdaBoostClassifier
from sklearn.linear_model.base import LinearRegression
from sklearn.linear_model.coordinate_descent import Lasso

from sklearn.linear_model.logistic import LogisticRegression
from sklearn.linear_model.ridge import Ridge
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm.classes import SVR
from sklearn.tree import DecisionTreeClassifier


DECISION_TREE = DecisionTreeClassifier()
LOGISTIC_REGRESSION = LogisticRegression()
NAIVE_BAYS = GaussianNB()

K_N_N = KNeighborsClassifier()
SUPPORT_VECTOR = svm.SVC(kernel="linear")

# Ensemble classifiers
RANDOM_FOREST = RandomForestClassifier(n_estimators=100)
GRADIENT_BOOST_CL = GradientBoostingClassifier(n_estimators=100)
ADA_BOOST = AdaBoostClassifier(n_estimators=100)
EXTRA_TREE = ExtraTreesClassifier(n_estimators=100)


# Regressors
GRADIENT_BOOST_RG = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
LINEAR_RG = LinearRegression()
RIDGE_RG = Ridge()
LASSO_RG = Lasso()
SVR_RG = SVR()

def getClassifierMap():
    CLASSIFIER_MAP = {
    "DECISION_TREE": DECISION_TREE,
    "LOGISTIC_REGRESSION": LOGISTIC_REGRESSION,
    "NAIVE_BAYS": NAIVE_BAYS,
    "K_N_N": K_N_N,
    "SUPPORT_VECTOR": SUPPORT_VECTOR,
    "RANDOM_FOREST": RANDOM_FOREST,
    "GRADIENT_BOOST": GRADIENT_BOOST_CL,
    "ADA_BOOST": GRADIENT_BOOST_CL,
    "EXTRA_TREE": EXTRA_TREE
    }
    return CLASSIFIER_MAP

def getRegressorMap():
    REGRESSOR_MAP = {
    "LINEAR_RG": LINEAR_RG,
    "RIDGE_RG": RIDGE_RG,
    "LASS0_RG": LASSO_RG,
    "SVR_RG": SVR_RG,
    "GRADIENT_BOOS_RG": GRADIENT_BOOST_RG,
    "RANDOM_FOREST": RANDOM_FOREST
    }
    return REGRESSOR_MAP
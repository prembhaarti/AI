# Decision Tree Classifier
from sklearn import datasets

import ClassifierList as CL
from algo.modelling import ModelAnalyser
from visualisation.bar_chart_demo import *

from sklearn import datasets

import ClassifierList as CL
from algo.modelling import ModelAnalyser
from visualisation.bar_chart_demo import *


# load the iris datasets
dataset = datasets.load_iris()
test_feature = [[5.2, 3.4, 1.3, 0.3]]

CLASSIFIER_MAP = {"DECISION_TREE": CL.DECISION_TREE,
                   "LOGISTIC_REGRESSION": CL.LOGISTIC_REGRESSION,
                   "NAIVE_BAYS": CL.NAIVE_BAYS,
                   "K_N_N": CL.K_N_N,
                   "SUPPORT_VECTOR": CL.SUPPORT_VECTOR,
                   "RANDOM_FOREST": CL.RANDOM_FOREST,
                  "GRADIENT_BOOST": CL.GRADIENT_BOOST,
                  "ADA_BOOST": CL.GRADIENT_BOOST,
                  "EXTRA_TREE": CL.EXTRA_TREE}

algo_score = ModelAnalyser.getCrossValScoreByClassifierList(CLASSIFIER_MAP, dataset)

rects, pl = visualize(algo_score.keys(), algo_score.values(),
                     xlabel="Algorithms", ylabel="Cross Validation score",
                     title="Classifiers Comparison", orientation="vertical")

for rect in rects:
    width = rect.get_width()
    height = rect.get_height()
    plt.text(rect.get_x()*10+width,rect.get_y()+width/3,width,ha='center',va='bottom')

pl.show()

# my_model.train(dataset.data, dataset.target)
# print my_model.getCrossValScore()
# plt.scatter(dataset.data,dataset.target,edgecolors="black")
# print my_model.predict(test_feature)

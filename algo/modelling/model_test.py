# Decision Tree Classifier
from sklearn import datasets

import ClassifierList as CL
from CommonModel import *
from visualisation.bar_chart_demo import *

# load the iris datasets
dataset = datasets.load_iris()
test_feature = [[5.2, 3.4, 1.3, 0.3]]

CLASSIFIER_LIST = {"DECISION_TREE": CL.DECISION_TREE,
                   "LOGISTIC_REGRESSION": CL.LOGISTIC_REGRESSION,
                   "NAIVE_BAYS": CL.NAIVE_BAYS,
                   "K_N_N": CL.K_N_N,
                   "SUPPORT_VECTOR": CL.SUPPORT_VECTOR,
                   "RANDOM_FOREST": CL.RANDOM_FOREST}

algo_score ={}
for k,v in CLASSIFIER_LIST.items():
    my_model = CommonModel(v, dataset)
    my_model.train(dataset.data, dataset.target)
    algo_score[k]=my_model.getCrossValScore()

rects, pl = visualize(algo_score.keys(),algo_score.values(),
                     xlabel="Algorithms",ylabel="Cross Validation score",
                     title="Classifiers Comparison",orientation="vertical")
for rect in rects:
    width = rect.get_width()
    height = rect.get_height()
    plt.text(rect.get_x()*10+width,rect.get_y()+width/3,width,ha='center',va='bottom')

pl.show()

# my_model.train(dataset.data, dataset.target)
# print my_model.getCrossValScore()
# plt.scatter(dataset.data,dataset.target,edgecolors="black")
# print my_model.predict(test_feature)

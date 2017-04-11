from collections import OrderedDict

from algo.modelling import ClassifierList as CL
from algo.modelling.CommonModel import CommonModel
from visualisation.bar_chart_demo import *


def getCrossValScoreByClassifierList(classifierMap, dataset):
    algo_score ={}

    # todo: sort the algo score by their score as descending
    for k,v in classifierMap.items():
        my_model = CommonModel(v, dataset)
        my_model.train(dataset.data, dataset.target)
        algo_score[k] = my_model.getCrossValScore()
        sorted_algo_score = OrderedDict(sorted(algo_score.items(), key=lambda x: x[1]))
    return sorted_algo_score

def getCrossValScoreByClassifierList(classifierMap, features, labels):
    algo_score ={}

    # todo: sort the algo score by their score as descending
    for k,v in classifierMap.items():
        my_model = CommonModel(v, features, labels)
        my_model.train(features, labels)
        score=my_model.getCrossValScore()
        algo_score[k] = score
        print (k," score:", score)
        sorted_algo_score = OrderedDict(sorted(algo_score.items(), key=lambda x: x[1]))
    return sorted_algo_score

def getRankingByClassifier(features, label):
    CLASSIFIER_MAP = CL.getClassifierMap()
    algo_score = getCrossValScoreByClassifierList(CLASSIFIER_MAP, features, label)

    rects, pl = visualize(algo_score.keys(), algo_score.values(),
                          xlabel="Algorithms", ylabel="Cross Validation score",
                          title="Classifiers Comparison", orientation="vertical")

    for rect in rects:
        width = rect.get_width()
        height = rect.get_height()
        plt.text(rect.get_x()*10+width,rect.get_y()+width/3,width,ha='center',va='bottom')

    pl.show()
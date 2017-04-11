import pandas as pd

from algo.feature_selection.Feature_Sel import selectKBest
from preprocessing import DataPreprocessing
from algo.modelling import ModelAnalyser
# load train and test data
titanic_data = pd.read_csv("train.csv")
titanic_test = pd.read_csv("test.csv")

# print titanic_data.columns.values

DataPreprocessing.imputateByMean(titanic_data,'Age')

# titanic_data=DataPreprocessing.dropEmptyRows(titanic_data,['Age'])

titanic_data = DataPreprocessing.replaceByMap(titanic_data, 'Sex', {'male': 0, 'female': 1})

titanic_label= titanic_data['Survived']
titanic_features = DataPreprocessing.getNumericalColumns(titanic_data)
DataPreprocessing.dropColumns(titanic_features, ['PassengerId','Survived'])

print selectKBest(titanic_features,titanic_label,k=5)


print DataPreprocessing.getNumericalColumnNames(titanic_features)
ModelAnalyser.getRankingByClassifier(titanic_features, titanic_label)

# print titanic_features.columns.value

# get basic info about dataset
# print DataPreprocessing.getInitialStats(titanic_data)
# DataPreprocessing.printInitialStats(titanic_data)


# finding unique values of each columns
# unique % and missing %
# transformed dataframe should be saved


# imputation

# mapping Non-numerical nominal values to integer

# check if any column can be decomposed

# check which features to choose for modelling

# apply algorithms and see the scores of predicting


# predict the test data and verify

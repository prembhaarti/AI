from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
import numpy as np

from preprocessing import DataPreprocessing


# def selectKBest(features, labels, k):
#     print features.head(2)
#     dataframe=SelectKBest(chi2, k=k).fit_transform(features, labels)
#     print dataframe[0:2]
#     print type(features)
#     print type(dataframe)
#     return dataframe

def selectKBest(features, labels, k, testSize=10):
    testBaseDataframe = features.head(testSize)
    columnNames=features.columns.values.tolist()
    resultColumpList=[]
    dataframe=SelectKBest(chi2, k=k).fit_transform(features, labels)
    resultDataFrame=dataframe[0:testSize]
    for colIndex in range(0,resultDataFrame.shape[1]):
        for columnName in columnNames:
            if np.array_equal(resultDataFrame[:, colIndex], testBaseDataframe[columnName].as_matrix().astype(float)):
                resultColumpList.append(columnName)
                DataPreprocessing.dropColumns(testBaseDataframe, [columnName])
                columnNames.remove(columnName)
    return resultColumpList

def selectFeaturesByPercentile(features,labels,percentile=80):
    return SelectPercentile(chi2, percentile=percentile).fit_transform(features, labels)
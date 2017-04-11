import numpy as np


def replaceByMap(dataframe, columnName, mapper):
    dataframe[columnName] = dataframe[columnName].map(mapper)
    return dataframe


def getCountOfValues(dataframe, columnName, ascending=False):
    return dataframe.groupby(columnName)[columnName].count().sort_values(ascending=ascending)


def imputateByValue(dataframe,columnName, valueToFill):
    dataframe[columnName]=dataframe[columnName].fillna(valueToFill)


def imputateByMean(dataframe, columnName):
    dataframe[columnName]=dataframe[columnName].fillna(dataframe[columnName].mean())


def imputateByMax(dataframe, columnName):
    dataframe[columnName]=dataframe[columnName].fillna(dataframe[columnName].max())

def dropEmptyRows(dataframe, columnNames):
    prev_rows=dataframe.shape[0]
    dataframe=dataframe.dropna(subset = columnNames)
    print "Rows deleted:", (prev_rows-dataframe.shape[0])
    return dataframe

def fillEmptyByMin(dataframe, columnName):
    dataframe[columnName]=dataframe[columnName].fillna(dataframe[columnName].min())


def convertToType(dataframe, columnName,type):
    dataframe[columnName] = dataframe[columnName].astype(type)


def getEmptyColumnCounts(dataframe):
    columnNames = np.array(dataframe.columns)
    columnMapCount = {}
    for columnName in columnNames:
        count = dataframe[columnName].isnull().sum()
        if count > 0:
            columnMapCount[columnName] = count
    return columnMapCount


def getNumericalColumnNames(dataframe):
    return dataframe.select_dtypes(include=[np.number]).columns.values

def getNumericalColumns(dataframe):
    return dataframe.select_dtypes(include=[np.number])


def getNonNumericalColumnNames(dataframe):
    # numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    return dataframe.select_dtypes(exclude=[np.number]).columns.values

def getNonNumericalColumns(dataframe):
    # numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    return dataframe.select_dtypes(exclude=[np.number])

def getInitialStats(dataframe):
    numericalColSize=len(getNumericalColumnNames(dataframe))
    nonNumericalColSize= len(getNonNumericalColumnNames(dataframe))
    print "Numerical Columns:", numericalColSize
    print dataframe[getNumericalColumnNames(dataframe)].head(1)
    print "\nNon-Numerical Columns:", nonNumericalColSize
    print dataframe[getNonNumericalColumnNames(dataframe)].head(1)
    print "\nEmpty series counts:", getEmptyColumnCounts(dataframe)

    print dataframe[getNumericalColumnNames(dataframe)].describe()

def printInitialStats(dataframe,fileName="initialStats.txt"):
    file= open(fileName,"w")
    numericalColSize=len(getNumericalColumnNames(dataframe))
    nonNumericalColSize= len(getNonNumericalColumnNames(dataframe))
    file.write("\nNumerical Columns:" + str(numericalColSize))
    file.write("\n"+str(dataframe[getNumericalColumnNames(dataframe)].head(1)))
    file.write("\n\nNon-Numerical Columns:" + str(nonNumericalColSize))
    file.write("\n"+str(dataframe[getNonNumericalColumnNames(dataframe)].head(1)))
    file.write("\n\nEmpty series counts:" + str(getEmptyColumnCounts(dataframe)))
    file.write("\n Column unique value counts:" + str(getUniqueStats(dataframe)))

    file.write("\n\n"+str(dataframe[getNumericalColumnNames(dataframe)].describe()))
    file.close()

def dropColumns(dataframe, columnNames):
    dataframe.drop(columnNames, axis=1, inplace=True)

def getUniqueStats(dataframe):
    columns= dataframe.columns.values
    columnMap={}
    for column in columns:
        columnMap[column]=len(dataframe[column].unique())
    return columnMap
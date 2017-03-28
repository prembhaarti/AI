# Decision Tree Classifier
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

# load the iris datasets
dataset = datasets.load_iris()

#list example of dataset
# sepal length, sepal width, petal length, petal width
# [[ 5.1  3.5  1.4  0.2]
#  [ 4.9  3.   1.4  0.2]
# [ 4.7  3.2  1.3  0.2]
# [ 4.6  3.1  1.5  0.2]
# [ 5.   3.6  1.4  0.2]
# [ 5.4  3.9  1.7  0.4]
# [ 4.6  3.4  1.4  0.3]
# [ 5.   3.4  1.5  0.2]
# [ 4.4  2.9  1.4  0.2]
# [ 4.9  3.1  1.5  0.1]
# [ 5.4  3.7  1.5  0.2]
# [ 4.8  3.4  1.6  0.2]
# [ 4.8  3.   1.4  0.1]
# [ 4.3  3.   1.1  0.1]
# [ 5.8  4.   1.2  0.2]
# [ 5.7  4.4  1.5  0.4]
# [ 5.4  3.9  1.3  0.4]
# [ 5.1  3.5  1.4  0.3]]
# print dataset.data

# dataset target :
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 ]
# 0 -> l. setosa
# 1 -> l. versicolor
# 2 -> l. verginica

# fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)

# make predictions
# expected = dataset.target
sample_data_to_predict = [[5.2, 3.4, 1.3, 0.3]]
predicted = model.predict(sample_data_to_predict)
print predicted
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
iris = load_iris()


X, y = iris.data, iris.target
print(X.shape)
print (iris.feature_names)
print X[0]

X_new = SelectPercentile(chi2,percentile=90).fit_transform(X, y)
print(X_new[0])



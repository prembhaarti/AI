import matplotlib.pyplot as plt

from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

k_means = cluster.KMeans(n_clusters=2)
k_means.fit(X_iris)

print(k_means.labels_[::10])

print(y_iris[::10])

plt.scatter(X_iris[0],X_iris[1],X_iris[2],X_iris[3]y_iris)
# plt.plot(X_iris, y_iris)
# plt.show()

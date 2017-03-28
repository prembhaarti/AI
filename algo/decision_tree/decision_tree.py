import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

from sklearn.externals.six import StringIO
import pydotplus


# loading dataset
iris = load_iris()

# for row in iris:
#     print row

# just displaying some data
print ("feature name:", iris.feature_names) #printing features name
print ("first data:", iris.data[0])		 #printing first data/row
print ("target names:", iris.target_names)	 #print labels/outputs

# training data
test_idx = [0, 50, 100]						 # created simple array
train_target = np.delete(iris.target, test_idx)	#took target data and deleted test_idx elements from them
train_data = np.delete(iris.data, test_idx, axis=0) # took data and deleted test_idx

# now look into first data
print ("printing first data again:", iris.data[0])		 #printing first data/row


#testing data
test_target = iris.target[test_idx]
# test_data = iris.data[test_idx]
test_data= [[ 5.1,  3.5,  1.4,  0.2]]


clf=tree.DecisionTreeClassifier() 
clf=clf.fit(iris.data, iris.target)	#Build a decision tree classifier from the training set (X, y).
clf=clf.fit(train_data, train_target)

print (test_target)
print (clf.predict(test_data))

# visualising the data
dot_data= StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, impurity=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris2.pdf")

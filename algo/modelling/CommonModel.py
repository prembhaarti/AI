from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

class CommonModel:

    def __init__(self, classifier):
        self.classifier = classifier

    def __init__(self, classifier, dataset):
        self.classifier = classifier
        self.dataset = dataset
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def train(self, features, labels, test_size=1.0):
        if test_size >= 1.0:
            self.classifier = self.classifier.fit(features, labels)
        else:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(features, labels, test_size=test_size, random_state=0)
            self.classifier = self.classifier.fit(self.X_train, self.y_train)

    def predict(self, test_features):
        return self.classifier.predict(test_features)

    def getScore(self):
        return self.classifier.score(self.X_test, self.y_test)

    def getCrossValScore(self,kfolds=5):
        scores = cross_val_score(self.classifier, self.dataset.data, self.dataset.target, cv=kfolds)
        return scores.mean()

    def visualize(self):
        pass

    def test(self):
        pass


    def getClassifier(self):
        return self.classifier

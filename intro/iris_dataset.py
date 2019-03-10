from sklearn.datasets import load_iris
iris_dataset = load_iris()
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0
)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
# print(iris_dataset['DESCR'][:193] + "\n...")
# print("type of target: {}".format(iris_dataset['target']))
# print("X_train shape: {}".format(X_train.shape))
# print("y_train shape: {}".format(y_train.shape))
# print("y_train: {}".format(y_train))

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
# iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# create a scatter matrix from the dataframe, color by y_train
# pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8)

knn.fit(X_train, y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=1, n_neighbors=1, p=2, weights='uniform')

X_new = np.array([[5, 2.9, 1, 0.2]])
# print ("X_new shape: {}".format(X_new.shape))

prediction = knn.predict(X_new)
# print("Prediction: {}".format(prediction))
# print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))

y_pred = knn.predict(X_test)
print("Test set predictions: \n {}".format(y_pred))
print("Actual test set: {}".format(y_test))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score using score method: {:.2f}".format(knn.score(X_test, y_test)))
print(y_pred == y_test)
from sklearn.linear_model import Lasso
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
lasso = Lasso().fit(X_train, y_train)
print("Training set socre: {:2f}".format(lasso.score(X_train, y_train)))
print ("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
# data/load_data.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def load_iris_data(test_size=0.2, random_state=42):
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test, iris.target_names

def explore_data():
    iris = load_iris()
    print("Dataset Shape:", iris.data.shape)
    print("Feature Names:", iris.feature_names)
    print("Target Classes:", iris.target_names)
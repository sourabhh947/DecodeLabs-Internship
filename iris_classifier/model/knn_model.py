from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def build_model(n_neighbors=5):
    """
    PDF: 'The Algorithm: K-Nearest Neighbors'
    Proximity Principle: similar things exist in close proximity.

    K=1   → overfitting  (noise)
    K=5   → optimal      (The Elbow — PDF)
    K=100 → underfitting (too generic)

    PDF Workflow Step 1: INSTANTIATE (Build the frame)
    """
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    return model


def train_model(model, X_train, y_train):
    """
    PDF Workflow Step 2: FIT (Memorize the map)
    KNN stores all training points — prediction happens at query time.
    """
    model.fit(X_train, y_train)
    print(f"Model trained on {len(X_train)} samples")
    return model


def predict(model, X_test):
    """
    PDF Workflow Step 3: PREDICT (Apply logic)
    For each test point: find K nearest neighbors → majority vote → class.
    """
    predictions = model.predict(X_test)
    print(f"Predictions made for {len(X_test)} test samples")
    return predictions


def find_best_k(X_train, y_train, X_test, y_test, k_range=range(1, 21)):
    """
    PDF: 'Tuning The Engine: Choosing K'
    Elbow Method — test K=1 to 20, find lowest error rate.
    """
    error_rates = []

    for k in k_range:
        knn  = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        pred  = knn.predict(X_test)
        error = 1 - accuracy_score(y_test, pred)
        error_rates.append(error)
        print(f"K={k:2d} | Error Rate: {error:.4f}")

    best_k = k_range[error_rates.index(min(error_rates))]
    print(f"\nBest K (The Elbow): {best_k}")
    return best_k, error_rates


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from data.load_data  import load_iris_data
    from data.preprocess import split_data, scale_features

    X, y, df, class_names      = load_iris_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_sc, X_test_sc, _   = scale_features(X_train, X_test)

    model       = build_model(n_neighbors=5)
    model       = train_model(model, X_train_sc, y_train)
    predictions = predict(model, X_test_sc)

    print("\nPredictions:", predictions[:10])
    print("Actual:     ", y_test[:10])
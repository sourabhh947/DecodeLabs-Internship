from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def split_data(X, y):
    """
    PDF: 'Structural Integrity: The Split'
    80% training, 20% testing.
    shuffle=True removes order bias (PDF requirement).
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        train_size=0.8,
        shuffle=True,
        random_state=42
    )

    print(f"Training samples : {len(X_train)} (80%)")
    print(f"Testing samples  : {len(X_test)}  (20%)")

    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """
    PDF: 'The Gatekeeper Rule: Scaling'
    StandardScaler — Mean=0, Variance=1.

    IMPORTANT RULE:
    - fit_transform() only on X_train
    - transform() only on X_test  (no data leakage)
    """
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from data.load_data import load_iris_data

    X, y, df, class_names = load_iris_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_sc, X_test_sc, scaler   = scale_features(X_train, X_test)

    print("\nBefore Scaling:", X_train[0].round(2))
    print("After  Scaling:", X_train_sc[0].round(2))
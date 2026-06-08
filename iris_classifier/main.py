# main.py

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from data.load_data import load_iris_data, explore_data

# Load data
X_train, X_test, y_train, y_test, flower_names = load_iris_data()

# Optional: explore
# explore_data()

# Train model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Data Classification Using AI")
print("-" * 35)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Sample predictions
samples = [
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.7, 4.1, 1.3],
    [6.7, 3.1, 5.6, 2.4],
]

print("\nSample Flower Predictions:")
print("-" * 35)
for sample in samples:
    prediction = model.predict([sample])
    print(f"Input: {sample} → Predicted: {flower_names[prediction[0]]}")
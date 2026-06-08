Project 2: Data Classification Using AI
DecodeLabs Industrial Training Kit | Batch 2026

What This Project Does
Trains a KNN (K-Nearest Neighbors) model to classify Iris flowers into 3 species:

Setosa
Versicolor
Virginica

Based on 4 measurements: sepal length, sepal width, petal length, petal width.

File Structure
iris_classifier/
├── main.py              ← Entry point — run this
└── data/
    ├── __init__.py      ← Empty file (required)
    └── load_data.py     ← Loads and splits Iris dataset

Setup & Run
Step 1 — Install dependencies
bashpip install scikit-learn pandas numpy
Step 2 — Run the project
bashpython main.py

Expected Output
Data Classification Using AI
-----------------------------------
Model Accuracy: 100.0 %

Sample Flower Predictions:
-----------------------------------
Input: [5.1, 3.5, 1.4, 0.2] → Predicted: setosa
Input: [6.0, 2.7, 4.1, 1.3] → Predicted: versicolor
Input: [6.7, 3.1, 5.6, 2.4] → Predicted: virginica

How It Works
StepWhat HappensCode1Load Iris dataset (150 samples, 4 features, 3 classes)load_iris()2Split into 80% train / 20% testtrain_test_split()3Train KNN model with K=5model.fit()4Predict on test datamodel.predict()5Check accuracyaccuracy_score()

Dataset Info
PropertyValueTotal Samples150Features4 (sepal length, sepal width, petal length, petal width)Classes3 (Setosa, Versicolor, Virginica)Train Size120 (80%)Test Size30 (20%)

Algorithm: K-Nearest Neighbors (KNN)

How it works: For a new data point, find the K=5 nearest training points by distance. Majority class among those 5 = prediction.
Why K=5: Balances overfitting (K=1) and underfitting (K=100).
Key metric: Accuracy score on unseen test data.


Tech Stack
ToolPurposePythonProgramming languagescikit-learnKNN model, dataset, train-test splitpandasData handlingnumpyNumerical operations

Project by DecodeLabs — Batch 2026
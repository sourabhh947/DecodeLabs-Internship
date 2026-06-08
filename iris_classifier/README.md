# 🌸 Iris Classifier

## Project 2: Data Classification Using AI

**DecodeLabs Industrial Training Kit | Batch 2026**

---

## 📖 Overview

This project demonstrates a machine learning classification task using the **K-Nearest Neighbors (KNN)** algorithm. The model is trained on the famous **Iris Dataset** and predicts the species of an iris flower based on its physical measurements.

The classifier can identify three species of iris flowers:

* Setosa
* Versicolor
* Virginica

using the following features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

---

## 📂 Project Structure

```text
## 📂 Project Structure

```text
iris_classifier/
│
├── main.py                     # Main entry point
├── README.md                   # Project documentation
│
├── data/
│   ├── __init__.py
│   ├── load_data.py            # Load Iris dataset
│   └── preprocess.py           # Data preprocessing
│
├── model/
│   ├── __init__.py
│   └── knn_model.py            # KNN model training and prediction
│
└── evaluation/
    ├── __init__.py
    └── evaluate.py             # Model evaluation and accuracy
```

```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd iris_classifier
```

### 2. Install Dependencies

```bash
pip install scikit-learn pandas numpy
```

---

## ▶️ Running the Project

Execute the following command:

```bash
python main.py
```

---

## 📌 Sample Output

```text
Data Classification Using AI

Model Accuracy: 100.0%

Sample Flower Predictions:

Input: [5.1, 3.5, 1.4, 0.2] → Predicted: Setosa
Input: [6.0, 2.7, 4.1, 1.3] → Predicted: Versicolor
Input: [6.7, 3.1, 5.6, 2.4] → Predicted: Virginica
```

---

## 🔍 How the Project Works

| Step | Description                                      |
| ---- | ------------------------------------------------ |
| 1    | Load the Iris dataset                            |
| 2    | Split the dataset into training and testing sets |
| 3    | Train the KNN model (K = 5)                      |
| 4    | Make predictions on test data                    |
| 5    | Evaluate model accuracy                          |

---

## 📊 Dataset Information

| Property         | Value     |
| ---------------- | --------- |
| Total Samples    | 150       |
| Features         | 4         |
| Classes          | 3         |
| Training Samples | 120 (80%) |
| Testing Samples  | 30 (20%)  |

### Features Used

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## 🤖 Machine Learning Algorithm

### K-Nearest Neighbors (KNN)

KNN is a supervised machine learning algorithm used for classification tasks.

### Working Principle

1. Calculate the distance between a new data point and all training samples.
2. Select the **K nearest neighbors**.
3. Determine the majority class among those neighbors.
4. Assign that class to the new data point.

### Why K = 5?

* Reduces overfitting compared to K = 1.
* Provides better generalization.
* Maintains a balance between bias and variance.

### Evaluation Metric

The model performance is measured using:

* **Accuracy Score**

which represents the percentage of correctly classified samples.

---

## 🛠️ Technologies Used

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| Python       | Programming Language     |
| Scikit-learn | Machine Learning Library |
| Pandas       | Data Processing          |
| NumPy        | Numerical Computation    |

---

## 🎯 Learning Outcomes

Through this project, you will learn:

* Data loading and preprocessing
* Train-test dataset splitting
* Classification using KNN
* Model evaluation using accuracy metrics
* Basic machine learning workflow in Python

---


---

## 📜 License

This project is created for educational and learning purposes under the DecodeLabs Industrial Training Program.

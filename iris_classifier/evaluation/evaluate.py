from sklearn.metrics import (
    confusion_matrix,
    f1_score,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score
)
import numpy as np


def evaluate_model(y_test, predictions, class_names):
    """
    PDF OUTPUT: Confusion Matrix + F1 Score
    PDF Warning: 'In imbalanced data, accuracy is a lie. We must look deeper.'
    """
    print("=" * 55)
    print("MODEL EVALUATION RESULTS")
    print("=" * 55)

    acc = accuracy_score(y_test, predictions)
    print(f"\nAccuracy : {acc:.4f} ({acc*100:.2f}%)")
    print("  WARNING: PDF calls this the 'Accuracy Mirage' alone!")

    print_confusion_matrix(y_test, predictions, class_names)
    print_metrics(y_test, predictions, class_names)

    return acc


def print_confusion_matrix(y_test, predictions, class_names):
    """
    PDF: 'The Diagnostic Tool: Confusion Matrix'
    TP = correct positive
    FP = False Alarm       (Type I Error)
    FN = Missed Detection  (Type II Error)
    TN = correct negative
    """
    cm = confusion_matrix(y_test, predictions)

    print("\n--- CONFUSION MATRIX ---")
    print("Rows = Actual | Columns = Predicted\n")

    header = "Actual / Predicted |"
    for name in class_names:
        header += f" {name[:10]:>10} |"
    print(header)
    print("-" * len(header))

    for i, row in enumerate(cm):
        row_str = f"{class_names[i]:>19} |"
        for val in row:
            row_str += f" {val:>10} |"
        print(row_str)

    print(f"\nCorrect: {np.trace(cm)} / {np.sum(cm)}")


def print_metrics(y_test, predictions, class_names):
    """
    PDF: 'Strategic Trade-Offs'
    Precision = Trustworthiness (Spam Filters use case)
    Recall    = Sensitivity     (Medical Diagnosis use case)
    F1 Score  = Harmonic Mean   (PRIMARY metric this project)
    """
    print("\n--- PRECISION, RECALL, F1 SCORE ---")
    print("(F1 = Harmonic Mean of Precision & Recall — PDF Primary Metric)\n")

    print(classification_report(y_test, predictions, target_names=class_names))

    f1        = f1_score(y_test, predictions, average='macro')
    precision = precision_score(y_test, predictions, average='macro')
    recall    = recall_score(y_test, predictions, average='macro')

    print(f"Overall F1 Score  (macro): {f1:.4f}  <- PRIMARY METRIC (PDF)")
    print(f"Overall Precision (macro): {precision:.4f}")
    print(f"Overall Recall    (macro): {recall:.4f}")

    return f1


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from data.load_data  import load_iris_data
    from data.preprocess import split_data, scale_features
    from model.knn_model import build_model, train_model, predict

    X, y, df, class_names            = load_iris_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_sc, X_test_sc, _         = scale_features(X_train, X_test)
    model       = build_model(n_neighbors=5)
    model       = train_model(model, X_train_sc, y_train)
    predictions = predict(model, X_test_sc)
    evaluate_model(y_test, predictions, class_names)
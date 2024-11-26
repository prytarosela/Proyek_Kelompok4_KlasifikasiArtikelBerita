from sklearn.metrics import classification_report
from joblib import load
from preprocess import load_and_preprocess_data

# Memuat model dan vectorizer
model = load("model/naive_bayes_model.joblib")
_, X_test, _, y_test, _ = load_and_preprocess_data()

# Evaluasi model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
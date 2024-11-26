from sklearn.naive_bayes import MultinomialNB
from joblib import dump
from preprocess import load_and_preprocess_data

# Memuat data dan preprocessing
X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess_data()

# Melatih model Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Menyimpan model dan vectorizer
dump(model, "model/naive_bayes_model.joblib")
dump(vectorizer, "model/tfidf_vectorizer.joblib")
print("Model dan vectorizer berhasil disimpan!")
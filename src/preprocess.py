import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def load_and_preprocess_data():
    # Memuat dataset
    from datasets import load_dataset
    dataset = load_dataset("ag_news")
    
    # Menggabungkan data menjadi DataFrame
    train_data = pd.DataFrame(dataset["train"])
    test_data = pd.DataFrame(dataset["test"])
    
    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=10000, stop_words="english")
    X_train = vectorizer.fit_transform(train_data["text"])
    X_test = vectorizer.transform(test_data["text"])
    
    y_train = train_data["label"]
    y_test = test_data["label"]
    
    return X_train, X_test, y_train, y_test, vectorizer
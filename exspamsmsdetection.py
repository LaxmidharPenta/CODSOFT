# =========================
# Spam SMS Detection Project
# Using Machine Learning
# Dataset: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
# =========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -------------------------
# Load and explore data
# -------------------------
data = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
data.columns = ["label", "message"]

# Encode labels: ham = 0, spam = 1
data["label_encoded"] = data["label"].map({"ham": 0, "spam": 1})

print(f"Total messages: {len(data)}")
print(data.head())

# Visualize class distribution
sns.countplot(x="label", data=data)
plt.title("Spam vs Ham Messages")
plt.show()

# -------------------------
# Train-test split
# -------------------------
X = data["message"]
y = data["label_encoded"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -------------------------
# Text vectorization
# -------------------------
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_features=3000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# -------------------------
# Define models
# -------------------------
models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Support Vector Machine": LinearSVC(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, random_state=42)
}

# -------------------------
# Train, predict, evaluate
# -------------------------
results = {}

for model_name, model in models.items():
    print(f"\nTraining {model_name}...")
    model.fit(X_train_tfidf, y_train)
    y_pred = model.predict(X_test_tfidf)
    
    accuracy = accuracy_score(y_test, y_pred)
    results[model_name] = accuracy
    
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Ham", "Spam"], yticklabels=["Ham", "Spam"])
    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# -------------------------
# Compare model performance
# -------------------------
print("\n=== Model Accuracy Comparison ===")
for name, acc in results.items():
    print(f"{name}: {acc:.4f}")

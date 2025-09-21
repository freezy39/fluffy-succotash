"""
Naive Bayes Classifier Project
CSC510 Module 6 Critical Thinking Assignment

This script implements a Naive Bayes classifier in Python using scikit-learn. 
It demonstrates:
- Converting data into frequency and likelihood tables
- Applying Laplacian correction
- Calculating posterior probabilities
- Predicting a class based on input features

Instructions:
1. Save your training data as a CSV file (example: camping_gear.csv).
   The CSV should contain categorical features (e.g., seats, legs, width, color) 
   and a target label column.
2. Run the script:
   python nb_classifier.py --csv camping_gear.csv
3. The script will output priors, likelihood tables, posterior probabilities, 
   and the predicted class for a query.

Justification:
Naive Bayes was chosen for this assignment because it is efficient, easy to 
implement, and performs well with categorical data, even when features are 
assumed independent. Laplacian correction ensures the model handles 
zero-probability issues. While simple, Naive Bayes provides interpretable 
results and is widely applied in classification problems such as spam 
filtering and text categorization (IBM, n.d.). This project demonstrates its 
use in categorizing camping furniture features into product types.

References:
IBM. (n.d.). Naive Bayes. IBM. https://www.ibm.com/topics/naive-bayes
Sharda, R., Delen, D., & Turban, E. (2023). Business intelligence, analytics, 
data science, and AI: A managerial perspective (5th ed.). Pearson.
"""

import argparse
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--csv", type=str, help="Path to CSV dataset")
args = parser.parse_args()

# Load dataset
if args.csv:
    df = pd.read_csv(args.csv)
else:
    # Demo dataset if no CSV provided
    data = {
        "color": ["green", "blue", "black", "tan", "green"],
        "style": ["folding", "sling", "folding", "folding", "folding"],
        "material": ["aluminum", "aluminum", "steel", "aluminum", "steel"],
        "label": ["chair", "chair", "chair", "cot", "cot"],
    }
    df = pd.DataFrame(data)
    print("Using demo dataset.")

print("\nHead:")
print(df.head())

# Separate features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Encode categorical variables
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Calculate class priors
class_counts = pd.Series(y).value_counts()
priors = class_counts / len(y)
print("\nClass frequency and priors:")
print(priors.to_frame("prior"))

# Likelihood tables with Laplace smoothing
for feature in X.columns:
    likelihood = pd.DataFrame()
    for label in y.unique():
        subset = df[df["label"] == label][feature]
        counts = subset.value_counts()
        smoothed = (counts + 1) / (len(subset) + len(df[feature].unique()))
        likelihood[label] = smoothed.reindex(df[feature].unique(), fill_value=1/(len(subset)+len(df[feature].unique())))
    print(f"\nFeature: {feature}")
    print(likelihood.T)

# Train Naive Bayes model
model = MultinomialNB(alpha=1.0)  # Laplace smoothing
model.fit(X, y_encoded)

# Example query
query = {"color": "green", "style": "folding", "material": "aluminum"}
query_encoded = []
for col in X.columns:
    if query[col] in encoders[col].classes_:
        query_encoded.append(encoders[col].transform([query[col]])[0])
    else:
        query_encoded.append(0)  # handle unknowns
query_encoded = np.array(query_encoded).reshape(1, -1)

# Predict
probs = model.predict_proba(query_encoded)[0]
pred_class = label_encoder.inverse_transform([np.argmax(probs)])[0]

print(f"\nQuery: {query}")
print("\nPredicted probabilities (scikit-learn):")
print(pd.Series(probs, index=label_encoder.classes_))
print(f"\nPredicted class: {pred_class}\n")
print("Done.")

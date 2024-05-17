from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import sys
from data_preprocessing import x_train, y_train, x_test, y_test

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# Assuming 'data_preprocessing.py' is located in a directory named 'decision_tree'
sys.path.append('decision_tree')

# Initialize the Decision Tree classifier
decision_tree = DecisionTreeClassifier()

# Train the classifier on the training data
decision_tree.fit(x_train, y_train)

# Predict on the test data
y_pred = decision_tree.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print()
print("Accuracy:", accuracy)
print("\nClassification Report:\n", report)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from data_preprocessing import x_train, y_train, x_test, y_test



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



print(y_pred == y_test)
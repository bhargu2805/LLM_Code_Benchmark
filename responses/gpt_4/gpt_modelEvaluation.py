from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Make predictions on the test set
y_pred = clf.predict(X_test)

# Step 2: Print accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {accuracy:.4f}")

# Step 3: Display the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)

# Step 4: Print classification report
class_report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(class_report)

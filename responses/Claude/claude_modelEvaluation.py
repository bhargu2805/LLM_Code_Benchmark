import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the processed DataFrame (ensure this is the scaled DataFrame from previous steps)
df = pd.read_csv('diabetes_processed.csv')  # Replace with actual path if needed

# Prepare the data (same as before)
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree Classifier (if not already done)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 1: Make predictions on the test set
y_pred = clf.predict(X_test)

# Step 2: Print the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy)

# Step 3: Display the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Step 4: Print the classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)
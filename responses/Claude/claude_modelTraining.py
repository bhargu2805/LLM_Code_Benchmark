import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the processed DataFrame (ensure this is the scaled DataFrame from previous steps)
df = pd.read_csv('diabetes_processed.csv')  # Replace with actual path if needed

# Step 1: Split the DataFrame into training and test sets (80-20 split)
X = df.drop('Outcome', axis=1)  # Features
y = df['Outcome']                # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 3: Print model parameters and confirm training completion
print("Model parameters:")
print(clf.get_params())
print("Training completed successfully.")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the CSV file into a pandas DataFrame
try:
    df = pd.read_csv('diabetes.csv')

    # Separate features (X) and target (y)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    # Split the data into training and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Decision Tree Classifier
    model = DecisionTreeClassifier(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Print model parameters
    print("Decision Tree Classifier Parameters:")
    print(model.get_params())
    print("\n")

    # Confirm training completion
    print("Decision Tree Classifier training completed successfully!")

except FileNotFoundError:
    print("Error: The file 'diabetes.csv' was not found. Make sure you have uploaded it to Colab.")
except Exception as e:
    print(f"An error occurred: {e}")
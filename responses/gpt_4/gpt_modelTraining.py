import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the processed dataset
df = pd.read_csv('diabetes.csv')

# Step 1: Encode 'Outcome' and scale the features
from sklearn.preprocessing import LabelEncoder, StandardScaler

label_encoder = LabelEncoder()
df['Outcome'] = label_encoder.fit_transform(df['Outcome'])

features = df.drop(columns=['Outcome'])
target = df['Outcome']

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Step 2: Split into training and test sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(
    scaled_features, target, test_size=0.2, random_state=42
)

# Step 3: Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 4: Print model parameters and confirm training
print("Model Parameters:")
print(clf.get_params())
print("\nTraining completed successfully.")

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the CSV file into a pandas DataFrame
try:
    df = pd.read_csv('diabetes.csv')

    # Initialize LabelEncoder
    label_encoder = LabelEncoder()

    # Encode the 'Outcome' column
    df['Outcome'] = label_encoder.fit_transform(df['Outcome'])
    print("DataFrame after Label Encoding 'Outcome':")
    print(df.head())
    print("\n")

    # Identify numeric features (excluding 'Outcome')
    numeric_features = df.columns.drop('Outcome')

    # Initialize StandardScaler
    scaler = StandardScaler()

    # Apply standard scaling to numeric features
    df[numeric_features] = scaler.fit_transform(df[numeric_features])

    # Display the transformed DataFrame
    print("Transformed DataFrame after Standard Scaling:")
    print(df.head())

except FileNotFoundError:
    print("Error: The file 'diabetes.csv' was not found. Make sure you have uploaded it to Colab.")
except Exception as e:
    print(f"An error occurred: {e}")
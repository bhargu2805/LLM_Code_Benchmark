import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Step 1: Encode the 'Outcome' column using LabelEncoder
label_encoder = LabelEncoder()
df['Outcome'] = label_encoder.fit_transform(df['Outcome'])

# Step 2: Apply StandardScaler to all numeric columns except 'Outcome'
features_to_scale = df.drop(columns=['Outcome'])
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_to_scale)

# Create a new DataFrame for the scaled features
scaled_df = pd.DataFrame(scaled_features, columns=features_to_scale.columns)

# Add the encoded Outcome column back
scaled_df['Outcome'] = df['Outcome']

# Step 3: Display the transformed DataFrame
print("Transformed DataFrame (first 5 rows):")
print(scaled_df.head())

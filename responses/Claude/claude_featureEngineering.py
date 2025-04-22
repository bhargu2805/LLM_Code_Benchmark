import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the CSV file into a DataFrame
df = pd.read_csv('diabetes.csv')

# Step 1: Encode the Outcome column using LabelEncoder
label_encoder = LabelEncoder()
df['Outcome'] = label_encoder.fit_transform(df['Outcome'])

# Step 2: Apply standard scaling to all numeric features except Outcome
scaler = StandardScaler()
numeric_features = df.drop('Outcome', axis=1)  # Exclude Outcome for scaling
scaled_features = scaler.fit_transform(numeric_features)

# Create a new DataFrame with scaled features and the encoded Outcome
df_scaled = pd.DataFrame(scaled_features, columns=numeric_features.columns)
df_scaled['Outcome'] = df['Outcome']

# Display the transformed DataFrame
print(df_scaled.head())
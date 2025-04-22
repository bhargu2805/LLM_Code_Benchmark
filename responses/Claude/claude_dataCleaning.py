import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('diabetes.csv')

# Step 1: Detect and print the number of missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Step 2: Drop rows with any missing values
df_cleaned = df.dropna()

# Step 3: Remove duplicate rows and print the number of rows removed
initial_shape = df_cleaned.shape
df_cleaned = df_cleaned.drop_duplicates()
rows_removed = initial_shape[0] - df_cleaned.shape[0]
print("Number of duplicate rows removed:", rows_removed)

# Step 4: Print the shape of the cleaned DataFrame
print("Shape of cleaned DataFrame:", df_cleaned.shape)
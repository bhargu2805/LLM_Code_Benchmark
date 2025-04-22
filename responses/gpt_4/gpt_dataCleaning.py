import pandas as pd

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Step 1: Detect and print the number of missing values in each column
print("Missing values in each column:")
print(df.isnull().sum())

# Step 2: Drop rows with any missing values
before_dropna = df.shape[0]
df = df.dropna()
after_dropna = df.shape[0]

# Step 3: Remove duplicate rows and report how many were removed
before_dedup = df.shape[0]
df = df.drop_duplicates()
after_dedup = df.shape[0]
rows_removed = before_dedup - after_dedup

print(f"\nRows removed due to missing values: {before_dropna - after_dropna}")
print(f"Rows removed as duplicates: {rows_removed}")

# Step 4: Print the final shape of the cleaned DataFrame
print("\nShape of the cleaned DataFrame:", df.shape)

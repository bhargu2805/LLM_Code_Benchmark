# Step 1: Upload file
from google.colab import files
uploaded = files.upload()


# Step 2: Load the uploaded CSV file using pandas
import pandas as pd

# Automatically detects the uploaded filename
df = pd.read_csv('diabetes.csv')

# Step 3: Display the first five rows
print("First five rows of the dataset:")
print(df.head())

# Step 4: Print shape and column names
print("\nShape of the DataFrame:", df.shape)
print("Column names:", df.columns.tolist())

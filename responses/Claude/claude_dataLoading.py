import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('diabetes.csv')

# Display the first five rows of the dataset
print(df.head())

# Print the shape of the DataFrame
print("Shape of DataFrame:", df.shape)

# List all column names
print("Column names:", df.columns.tolist())
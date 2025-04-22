import pandas as pd

# Load the CSV file into a pandas DataFrame
try:
    df = pd.read_csv('diabetes.csv')

    # Display the first five rows
    print("First five rows of the DataFrame:")
    print(df.head())
    print("\n")

    # Print the shape of the DataFrame
    print("Shape of the DataFrame:", df.shape)
    print("\n")

    # List all column names
    print("Column names:", df.columns.tolist())

except FileNotFoundError:
    print("Error: The file 'diabetes.csv' was not found. Make sure you have uploaded it to Colab.")
except Exception as e:
    print(f"An error occurred: {e}")
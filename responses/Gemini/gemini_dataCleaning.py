import pandas as pd

# Load the CSV file into a pandas DataFrame
try:
    df = pd.read_csv('diabetes.csv')

    # 1. Detect and print the number of missing values in each column
    print("Number of missing values per column:")
    print(df.isnull().sum())
    print("\n")

    # 2. Drop rows with any missing values
    initial_rows = df.shape[0]
    df_cleaned_missing = df.dropna()
    rows_dropped_missing = initial_rows - df_cleaned_missing.shape[0]
    print(f"Number of rows dropped due to missing values: {rows_dropped_missing}")
    print("\n")

    # 3. Remove duplicate rows (if any) and print the number of rows removed
    initial_rows_cleaned = df_cleaned_missing.shape[0]
    df_cleaned_duplicates = df_cleaned_missing.drop_duplicates()
    rows_dropped_duplicates = initial_rows_cleaned - df_cleaned_duplicates.shape[0]
    print(f"Number of duplicate rows removed: {rows_dropped_duplicates}")
    print("\n")

    # 4. Print the shape of the cleaned DataFrame
    print("Shape of the cleaned DataFrame:", df_cleaned_duplicates.shape)

except FileNotFoundError:
    print("Error: The file 'diabetes.csv' was not found. Make sure you have uploaded it to Colab.")
except Exception as e:
    print(f"An error occurred: {e}")
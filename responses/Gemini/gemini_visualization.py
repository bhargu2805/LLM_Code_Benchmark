import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
try:
    df = pd.read_csv('diabetes.csv')

    # 1. Create a histogram of the 'Glucose' column
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Glucose'], kde=True)
    plt.title('Distribution of Glucose Levels')
    plt.xlabel('Glucose')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # 2. Generate a seaborn pairplot of the entire dataset, colored by 'Outcome'
    plt.figure(figsize=(12, 12))
    sns.pairplot(df, hue='Outcome', diag_kind='kde', markers=['o', 's'])
    plt.suptitle('Pairplot of Diabetes Dataset (Colored by Outcome)', y=1.02)
    plt.show()

except FileNotFoundError:
    print("Error: The file 'diabetes.csv' was not found. Make sure you have uploaded it to Colab.")
except Exception as e:
    print(f"An error occurred: {e}")
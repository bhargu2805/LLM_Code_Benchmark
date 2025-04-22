import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the processed DataFrame (ensure this is the scaled DataFrame from previous steps)
df = pd.read_csv('diabetes_processed.csv')  # Replace with actual path if needed

# Set the style for the plots
sns.set(style="whitegrid")

# Step 1: Create a histogram of the Glucose column
plt.figure(figsize=(10, 6))
sns.histplot(df['Glucose'], bins=30, kde=True, color='blue')
plt.title('Histogram of Glucose Levels', fontsize=16)
plt.xlabel('Glucose Level', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)
plt.show()

# Step 2: Generate a seaborn pairplot of the entire dataset, colored by the Outcome column
plt.figure(figsize=(12, 10))
pairplot = sns.pairplot(df, hue='Outcome', palette='coolwarm', diag_kind='kde')
pairplot.fig.suptitle('Pairplot of Diabetes Dataset', y=1.02, fontsize=16)
plt.show()
# Step 1: Upload the file
from google.colab import files
uploaded = files.upload()



# Step 2: Import libraries and load data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('diabetes.csv')

# Step 3: Plot histogram of Glucose
plt.figure(figsize=(8, 5))
sns.histplot(df['Glucose'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Glucose Levels')
plt.xlabel('Glucose')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Generate seaborn pairplot colored by Outcome
sns.pairplot(df, hue='Outcome', corner=True, plot_kws={'alpha': 0.6})
plt.suptitle('Pairplot of Diabetes Dataset Colored by Outcome', y=1.02)
plt.show()

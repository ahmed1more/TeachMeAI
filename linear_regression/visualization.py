import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.chdir('linear_regression')  # Change this to the directory containing 'Student_Performance.csv'

# Read the CSV data into a DataFrame
df = pd.read_csv('Student_Performance.csv')

# Create a figure with 2 rows and 3 columns of subplots
fig, ax = plt.subplots(2, 3, figsize=(16, 10))

# Visualize each column's data
ax[0, 0].bar(df['Hours Studied'].unique(), df['Hours Studied'].value_counts())
ax[0, 0].set_title('Hours Studied Frequency')

ax[0, 1].hist(df['Previous Scores'], edgecolor="black")
ax[0, 1].set_title('Previous Scores Frequency')

ax[0, 2].bar(df['Sleep Hours'].unique(), df['Sleep Hours'].value_counts())
ax[0, 2].set_title('Sleep Hours Frequency')

ax[1, 0].bar(
    df['Sample Question Papers Practiced'].unique(),
    df['Sample Question Papers Practiced'].value_counts(),
)
ax[1, 0].set_title('Sample Question Papers Practiced')

ax[1, 1].hist(df['Performance Index'], edgecolor="black")
ax[1, 1].set_title('Performance Index')

# Adjust spacing to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()

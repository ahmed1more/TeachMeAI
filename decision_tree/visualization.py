import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
import seaborn as sns

os.chdir('decision_tree')

data = pd.read_csv('loan.csv')
# data.info()

red_palette = sns.color_palette("Reds_r")

# Visualization 1: Distribution of age
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', bins=20, kde=True, color=red_palette[-2])
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# Visualization 2: Count of loan status
plt.figure(figsize=(6, 6))
sns.countplot(data=data, x='loan_status', palette=red_palette)
plt.title('Count of Loan Status')
plt.xlabel('Loan Status')
plt.ylabel('Count')
plt.show()

# Visualization 3: Boxplot of income by loan status
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='loan_status', y='income', palette=red_palette)
plt.title('Income by Loan Status')
plt.xlabel('Loan Status')
plt.ylabel('Income')
plt.show()


# Visualization 4: Count of gender
plt.figure(figsize=(6, 6))
sns.countplot(data=data, x='gender', palette=red_palette)
plt.title('Count of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# Visualization 5: Count of education level
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='education_level', palette=red_palette)
plt.title('Count of Education Level')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.show()

# Visualization 6: Count of occupation
plt.figure(figsize=(10, 8))
sns.countplot(data=data, y='occupation', palette=red_palette)
plt.title('Count of Occupation')
plt.xlabel('Count')
plt.ylabel('Occupation')
plt.show()
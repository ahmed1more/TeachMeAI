import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os



os.chdir('decision_tree')

data = pd.read_csv("loan.csv")

data.drop_duplicates(keep='first', inplace=True)

def detect_outliers_iqr(data, k=1.5):
    """
    Detect outliers in a 1D array using the Interquartile Range (IQR) method.
    
    Parameters:
        data (array-like): 1D array or list containing the data.
        k (float): Multiplier for the IQR. Typically set to 1.5.
        
    Returns:
        outliers (array-like): 1D array containing the outliers.
    """
    # Calculate Q1 (25th percentile) and Q3 (75th percentile) of the data
    q1 = np.percentile(data['income'], 25)
    q3 = np.percentile(data['income'], 75)
    
    # Calculate the IQR (Interquartile Range)
    iqr = q3 - q1
    
    # Define the lower and upper bounds for outliers
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    
    # Identify outliers
    outliers = [x for x in data['income'] if x < lower_bound or x > upper_bound]
    
    return outliers


outliers = detect_outliers_iqr(data)
data = data[~data['income'].isin(outliers)]


data['gender'] = data['gender'].map({'Male': 1, 'Female':0})
data['loan_status'] = data['loan_status'].map({'Approved':1, 'Denied':0})
data['marital_status'] = data['marital_status'].map({'Married':1, 'Single':0})
df1 = pd.get_dummies(data, columns=['occupation', 'education_level'])

x = df1.drop('loan_status', axis=1)
y = df1['loan_status']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=90)
x_train.head()


columns_to_scale = ['age', 'income', 'credit_score']
scaler = StandardScaler()
x_train[columns_to_scale] = scaler.fit_transform(x_train[columns_to_scale])
x_test[columns_to_scale] = scaler.transform(x_test[columns_to_scale])





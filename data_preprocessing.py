import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler





data = pd.read_csv("loan.csv")

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





import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

os.chdir('linear_regression')
# print(os.getcwd())

data = pd.read_csv("Student_Performance.csv")

data.drop_duplicates(keep='first', inplace=True)
data.reset_index(drop=True, inplace=True)
# print(data.info())


# print(data['Extracurricular Activities'].unique())

data['Extracurricular Activities'] = data['Extracurricular Activities'].map({'Yes':1, 'No':0})
# print(data['Extracurricular Activities'].unique())

x = data.drop('Performance Index', axis=1)
y = data['Performance Index']
print(x.shape)
print(y.shape)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=90)
# x_train.head()



columns_to_scale = ['Previous Scores']
scaler = StandardScaler()
x_train[columns_to_scale] = scaler.fit_transform(x_train[columns_to_scale])
x_test[columns_to_scale] = scaler.transform(x_test[columns_to_scale])


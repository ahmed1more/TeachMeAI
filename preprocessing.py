import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler

def impute_data(data):
    # Identify numerical and categorical columns
    numerical_cols = data.select_dtypes(include=['number']).columns
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns

    # Impute missing numerical values with the mean
    if len(numerical_cols) > 0:
        imputer_num = SimpleImputer(strategy="mean")
        data[numerical_cols] = imputer_num.fit_transform(data[numerical_cols])

    # Impute missing categorical features with the most frequent value
    if len(categorical_cols) > 0:
        imputer_cat = SimpleImputer(strategy="most_frequent")
        data[categorical_cols] = imputer_cat.fit_transform(data[categorical_cols])

    return data

def encode_data(data, encoding_strategy="one-hot"):
    # Convert boolean values to integers
    boolean_cols = data.select_dtypes(include=['bool']).columns
    data[boolean_cols] = data[boolean_cols].astype(int)
    # Identify categorical columns (after handling boolean columns)
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns

    if encoding_strategy == "one-hot":
        data = pd.get_dummies(data, columns=categorical_cols)
        data = data.replace({True: 1, False: 0})

    elif encoding_strategy == "label":
        for col in categorical_cols:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])

    return data

def standardize_data(data):
    # Identify numerical columns
    numerical_cols = data.select_dtypes(include=['number']).columns
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the numerical columns
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    
    return data

def min_max_scale_data(data, feature_range=(0, 1)):
    # Identify numerical columns
    numerical_cols = data.select_dtypes(include=['number']).columns
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=feature_range)
    
    # Scale the numerical columns
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    
    return data

# Path to your CSV file
path = r"C:\Users\Ahmed\Desktop\ML-GUI\linear_regression\Student_Performance.csv"
data = pd.read_csv(path)
data.drop_duplicates(inplace=True)
print("Original data info:")
print(data.info())

# Impute missing values
data_imputed = impute_data(data)
print("Data after imputation:")
print(data_imputed.info())


# Standardize data
data_standardized = standardize_data(data_imputed)
print("Data after standardization:")
print(data_standardized.shape)
print(data_standardized)

# Encode categorical data
data_encoded = encode_data(data_standardized, encoding_strategy="label")
print("Data after encoding (one-hot):")
print(data_encoded.shape)
print(data_encoded.info())
print(data_encoded)



# حالة خاصة 
if "loan_status" in data_encoded.columns:
    data_encoded['loan_status'] = data_encoded["loan_status"].map({1: 0, 0: 1})





preProcessing_data = data_encoded.copy()
print(type(preProcessing_data))
preProcessing_data.to_csv("Pre_loan.csv", index=False,header=True)


from sklearn.preprocessing import OneHotEncoder

# Sample data (replace with your actual data)
data = ["cat", "dog", "rabbit", "cat", "bird", "dog"]

# Create a OneHotEncoder object
encoder = OneHotEncoder()

# Encode the data
encoded_data = encoder.fit_transform(data.reshape(-1, 1))

# Print the original data and encoded data (one-hot encoded)
print("Original data:", data)
print("One-hot encoded data:", encoded_data)

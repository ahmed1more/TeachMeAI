from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from preprocessing import x_train, y_train, x_test, y_test
import sys
sys.path.append('linear_regression')

# Ensure y_train and y_test are in the correct shape
y_train = y_train.ravel()
y_test = y_test.ravel()

model = LinearRegression()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

# Print the model parameters and metrics
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R² Score: {r2}")

np.random.seed(0)
random_numbers = np.random.randint(0, len(y_predict), size=15)
# Inspect the first few predictions
print("First 10 predictions vs actual values:")
for i in random_numbers:
    print(f"Predicted: {y_predict[i]}, Actual: {y_test[i]}")
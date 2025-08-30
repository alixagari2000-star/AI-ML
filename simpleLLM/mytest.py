import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Small data  (10 samples with 2 features)
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 8], [9, 10], [10, 11]])
y = np.dot(X, np.array([1, 2])) + 3

# Split the data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create linear regression object
lr_model = LinearRegression()

# Train the model using the training sets
lr_model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = lr_model.predict(X_test)

# The coefficients
print('Coefficients: \n', lr_model.coef_)
# The mean squared error
print('Mean Squared Error: %.2f'%mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of Determination (R-Squared): %.2f'%r2_score(y_test, y_pred))

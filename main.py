import numpy as np
import matplotlib.pyplot as plt

# Example data: number of female (X) and male (Y) births
X = np.array([2983, 3092, 3339, 3301, 3198, 3314, 3278, 2687, 2455, 2508, 2733])
Y = np.array([1389, 1425, 1473, 1444, 1514, 1508, 1487, 1287, 1200, 1221, 1204])

# Construct polynomial design matrix X_poly for linear regression
# Column 0: female births (X), Column 1: bias (constant term)
X_poly = np.zeros([len(X), 2])
for i in range(len(X)):
    X_poly[i, 0] = X[i]
    X_poly[i, 1] = 1

# Compute beta using the ordinary least squares formula
# beta = (X.T @ X)^(-1) @ X.T @ Y
beta = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ Y

# Get predicted values
Y_pred = X_poly @ beta

# Plot the real data and the regression line
plt.scatter(X, Y, color='blue', label='Observed Data')
plt.plot(X, Y_pred, color='red', label='Fitted Line')
plt.xlabel('Number of Female Births')
plt.ylabel('Number of Male Births')
plt.title('Correlation Between Male and Female Births')
plt.grid()
plt.legend()
plt.show()

# Print regression coefficients
print(f'Slope (beta_0): {beta[0]}')
print(f'Intercept (beta_1): {beta[1]}')

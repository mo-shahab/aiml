import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the kernel function
def kernel(point, xmat, k):
    m, n = np.shape(xmat)
    weights = np.mat(np.eye((m)))
    for j in range(m):
        diff = point - X[j]
        weights[j, j] = np.exp(diff * diff.T / (-2.0 * k**2))
    return weights

# Define the local weight calculation
def localWeight(point, xmat, ymat, k):
    wei = kernel(point, xmat, k)
    W = (X.T * (wei * X)).I * (X.T * (wei * ymat.T))
    return W

# Define the main localWeightRegression function
def localWeightRegression(xmat, ymat, k):
    m, n = np.shape(xmat)
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i] * localWeight(xmat[i], xmat, ymat, k)
    return ypred

# Load data points from a CSV file (tips.csv)
data = pd.read_csv('tips.csv')
bill = np.array(data.total_bill)
tip = np.array(data.tip)
mbill = np.mat(bill)
mtip = np.mat(tip)
m = np.shape(mbill)[1]
one = np.mat(np.ones(m))
X = np.hstack((one.T, mbill.T))

# Set the bandwidth parameter 'k' here
ypred = localWeightRegression(X, mtip, 0.5)

# Sort the data points for plotting
SortIndex = X[:, 1].argsort(0)
xsort = X[SortIndex][:, 0]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(bill, tip, color='yellow')
ax.plot(xsort[:, 1], ypred[SortIndex], color='black', linewidth=2)
plt.xlabel('Total bill')
plt.ylabel('Tip')
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kernel(point, xmat, k):
    m, n = np.shape(xmat)
    weight = np.mat(np.eye(m))
    for j in range(m):
        diff = point - xmat[j]
        weight[j,j] = np.exp(diff*diff.T / -2.0*k**2)
    return weight

def localweight(point, xmat, ymat, k):
    wei = kernel(point, xmat, k)
    w = (x.T*(wei*x)).I * (x.T*(wei*ymat.T))
    return w

def localweightregression(xmat, ymat, k):
    m, n = np.shape(xmat)
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i] * localweight(xmat[i], xmat, ymat, k)
    return ypred

data = pd.read_csv('tips.csv')

bill = np.array(data.total_bill)
tip = np.array(data.tip)

mbill = np.mat(bill)
mtip = np.mat(tip)

m = np.shape(mbill)[1]
one = np.mat(np.ones(m))
x = np.hstack((one.T, mbill.T))

ypred = localweightregression(x, mtip, 0.5)
sortindex = x[:,1].argsort(0)
xsort = x[sortindex][:,0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(bill, tip, color="yellow")
ax.plot(xsort[:,1], ypred[sortindex], color="black", linewidth=2)
plt.xlabel('total bill')
plt.ylabel('tip')
plt.show()

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

dataset = load_iris()

print("iris dataset\n", dataset.data)
print("iris features\n", dataset.feature_names)
print("iris targets: \n", dataset.target)
print("iris target names: \n", dataset.target_names)

x = pd.DataFrame(dataset.data)
y = pd.DataFrame(dataset.target)

x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y.columns= ['Targets']

print(y)

plt.figure(figsize=(8, 5))
colormap = np.array(['red', 'lime', 'blue'])

plt.subplot(1, 3, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=20)
plt.title('before clustering')

plt.subplot(1, 3, 2)
model = KMeans(n_clusters = 3)
model.fit(x)
predy = np.choose(model.labels_, [0, 1, 2]).astype(np.int64)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predy], s=20)
plt.title('kmeans')

plt.subplot(1, 3, 3)
scaler = preprocessing.StandardScaler()
scaler.fit(x)
xsa = scaler.transform(x)
xs = pd.DataFrame(xsa, columns=x.columns)
gmm= GaussianMixture(n_components=3)
gmm.fit(xs)
predy = gmm.predict(xs)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predy],  s=20)
plt.title('gaussian mixturee')

plt.show()

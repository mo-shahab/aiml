from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

assigned_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
data = pd.read_csv("iris2.csv", names=assigned_names) 

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.1)

classifier = KNeighborsClassifier(n_neighbors=5).fit(xtrain,ytrain)
ypred = classifier.predict(xtest)

i = 0
print("---------------------")
print("%-25s %-25s %-25s"%('original label', 'predicted label', 'correct/wrong'))
for label in ytest:
    print("%-25s %-25s"%(label, ypred[i]),end="")
    if (label == ypred[i]):
        print('%-25s'%('correct'))
    else:
        print('%-25s'%('wrong'))

    i = i+1

print("confusion matrix\n", metrics.confusion_matrix(ytest, ypred))
print("classification report\n", metrics.classification_report(ytest, ypred))

print('accuracy score: \n', metrics.accuracy_score(ytest, ypred))
plt.plot(xtest, ytest, 'ro')
plt.plot(xtest, ytest, 'b+')
plt.show()

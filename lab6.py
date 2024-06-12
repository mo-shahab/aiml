import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data = pd.read_csv("tennis.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

obj1 = LabelEncoder()
x.Outlook = obj1.fit_transform(x.Outlook)

obj2 = LabelEncoder()
x.Temperature = obj2.fit_transform(x.Temperature)

obj3 = LabelEncoder()
x.Humidity = obj3.fit_transform(x.Humidity)

obj4 = LabelEncoder()
x.Wind = obj4.fit_transform(x.Wind)

obj5 = LabelEncoder()
y = obj5.fit_transform(y)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
print(y)
classifier = GaussianNB()
classifier.fit(xtrain, ytrain)
ypred = classifier.predict(xtest)
print("this is the stuff idont know man", ypred)
print("this is the accuracy score and shit", accuracy_score(ypred, ytest))


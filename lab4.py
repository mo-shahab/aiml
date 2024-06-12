def find_entropy(df):
    class_ = df.keys()[-1]
    variables = df[class_].unique()
    entropy = 0
    for variable in variables:
        fraction = df[class_].value_counts()[variable] / len(df[class_])
        entropy += -fraction * np.log2(fraction)
    return entropy

def find_entropy_attribute(df, attribute):
    class_ = df.keys()[-1]
    targets = df[class_].unique()
    variables = df[attribute].unique()
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target in targets:
            num = len (
                    df[attribute][df[attribute] == variable][df[class_] == target]
                    )
            den = len(df[attribute][df[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * np.log2(fraction + eps)
        fraction2 = den/len(df)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)

def find_winner(df):
    ig = []
    for key in df.keys()[:-1]:
        ig.append(find_entropy(df) - find_entropy_attribute(df, key))
    return df.keys()[:-1][np.argmax(ig)]

def getsubtable(df, node, value):
    return df[df[node] == value].reset_index(drop=True)

def buildtree(df, tree=None):
    node = find_winner(df)
    attvalues = np.unique(df[node])
    if tree is None:
        tree = {}
        tree[node]= {}
    for value in attvalues:
        subtable = getsubtable(df, node, value)
        clvalue, counts = np.unique(subtable["Play"], return_counts=True)
        if len(counts) == 1:
            tree[node][value] = clvalue[0]
        else:
            tree[node][value] = buildtree(subtable)
    return tree

def func(test, tree, default=None):
    attribute = next(iter(tree))
    if test[attribute] in tree[attribute].keys():
        result = tree[attribute][test[attribute]]
        if isinstance (result, dict):
            return func(test, result)
        else:
            return result
    else:
        return default

import numpy as np
import pandas as pd

eps = np.finfo(float).eps
import pprint
from numpy import log2 as log
df = pd.read_csv("tennis.csv")
tree = buildtree(df)

pprint.pprint(tree)
test = {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High",
"Wind": "Weak"}

print(func(test, tree))



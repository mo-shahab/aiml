import numpy as np

x = np.array([[2, 9], [3, 5], [1, 6]], dtype=float)
y = np.array(([92], [86], [89]), dtype=float) / 100

i = 2
h = 3
o = 1

epochs = 5
lr = 0.1

wh = np.random.uniform(size=(i, h))
bh = np.random.uniform(size=(1, h))
wout = np.random.uniform(size=(h, o))
bout = np.random.uniform(size=(1, o))

for epoch in range(epochs):

    hinp= np.dot(x, wh) + bh
    hlayer = 1 / (1 + np.exp(-hinp))
    oinp = np.dot(hlayer, wout) + bout
    out = 1 / (1 + np.exp(-oinp))

    eo = y - out
    dout = eo * out * (1 - out)
    eh = dout.dot(wout.T)
    dhidd = eh * hlayer * (1 - hlayer)

    wout += hlayer.T.dot(dout) * lr
    wh += x.T.dot(dhidd) * lr

    print(x)
    print(y)
    print(out)

print(x)
print(y)
print(out)

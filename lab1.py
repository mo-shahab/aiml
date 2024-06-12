a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

k = 4
print(a)
print(a[k:])
print(list(reversed(a[:k+1])))
a[:k+1] = list(reversed(a[:k+1]))
print(a)
a[k+1:] = list(reversed(a[k+1:]))

a = list(reversed(a))
print(a)

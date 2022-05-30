import numpy as np

x = list(map(int, input().split()))
y = x[0]
arr = []
for i in range(y):
    a = list(map(int, input().split()))
    arr.append(a)

a = np.array(arr)
print(np.transpose(a))
print(a.flatten())

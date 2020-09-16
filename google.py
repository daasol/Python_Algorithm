import numpy as np
def y(x) :
    global a
    a=4
    return 0

def f(a) :
    a=3
    print(a)
    return a

a=5
f(a)
print(a)
y(a)
print(a)

arr = [1.4,3.7,4.8,6.3,99.9]
x = arr.pop(2)
print(x)

print(np.transpose([[1, 2, 3], [4, 5, 6]]))
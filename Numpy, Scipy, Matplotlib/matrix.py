import numpy as np
from scipy.linalg import lu


a = np.mat('1, 2; 3, 4; 5, 6')
print(a)

aT = np.transpose(a)
print(aT)

b = 2*np.eye(3)
print(b)

c = b*a
print(c)

l = lu(a)
print(l)
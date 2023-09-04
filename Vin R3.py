import numpy as np

v = [3, 4, 1]
v1 = [1, 2, 0]
v2 = [2, 4, 1]
v3 = [1, 1, 1]

A = np.matrix([v1, v2, v3]).T
[m, n] = np.shape(A)
r = np.linalg.matrix_rank(A)
b = np.array(v).reshape(-1, 1)

if r == n:
    coefficients = np.linalg.solve(A, b)
    linear_combination = (coefficients[0] * v1 + coefficients[1] * v2 + coefficients[2] * v3)
    print(linear_combination)
    print('v =', coefficients[0], '* v1 +', coefficients[1], ' * v2 +', coefficients[2], ' * v3')
else:
    print("It is not possible to express v as a linear combination of given vectors")

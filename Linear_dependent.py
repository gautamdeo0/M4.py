from sympy import *

A = Matrix([[-1, 2, 3, 1], [3, 4, 6, 1], [2, -1, 4, 1]]).T
[m, n] = A.shape  # m represents the number of rows
r = A.rank()

if r == n:
    print('Given vectors are linearly independent')
else:
    print('Given vectors are linearly dependent')

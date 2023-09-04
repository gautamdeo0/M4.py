from sympy import *

A = Matrix([[1, 2, 3, 1], [4, 8, 12, 4], [3, 6, 9, 3]])
display("Given matrix:", A)

[m, n] = A.shape
r = A.rank()
print('Rank of the linear transformation =', r)

NullSpace = A.nullspace()
nullity = len(NullSpace)
print('Nullity of the linear transformation =', nullity)

if r + nullity == n:
    print("Rank-nullity theorem holds.")
else:
    print("Rank-nullity theorem does not hold.")

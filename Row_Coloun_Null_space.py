from sympy import *
A = Matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
row_space = Matrix(A.rowspace())
col_space = Matrix([A.columnspace()])
display('Basis of row space are ',row_space)
display('Basis of column space are ',col_space)
print('dimension of Row Sapce=dimension of Column Sapce=',A.rank())
NSpace = A.nullspace()
display('The basis for Nullspace is',NSpace)
print('dimesion of Null Sapce=',len(NSpace))
import numpy as np
import matplotlib.pyplot as plt
u = np.array([[2],[0]])
v = np.array([[0],[3]])
w = np.array([[1],[3]])
c1= 1
c2= 2
c3= 3
V= c1*u + c2*v+c3*w
print(V)
plt.arrow(0,0, 2,0 , color='r',head_width=0.25, head_length=0.25)
plt.arrow(0,0, 0,3 , color='g',head_width=0.25, head_length=0.25)
plt.arrow(0,0, 1,3 , color='y',head_width=0.25, head_length=0.25)
plt.arrow(0,0,5,15 , color='r',head_width=0.25,head_length=0.25)
plt.grid()
plt.show()
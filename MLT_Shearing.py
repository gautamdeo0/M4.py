%matplotlib inline
from math import pi, sin, cos
import matplotlib.pyplot as plt
import numpy as np
coords = np.array([[0,0],[0.5,0.5],[0.5,1.5],[0,1],[0,0]])
coords = coords.transpose()
coords
x = coords[0,:]
y = coords[1,:]
A = np.array([[2,0],[0,1]])
A_coords = A@coords
S = np.array([[1,2],[0,1]])
S_coords = S@coords
x_LT4 = S_coords[0,:]
y_LT4 = S_coords[1,:]
# Create the figure and axes objects
fig, ax = plt.subplots()
# Plot the points. x and y are original vectors, x_LT1 and y_LT1 are images
ax.plot(x,y,'ro')
ax.plot(x_LT4,y_LT4,'bo')
# Connect the points by lines
ax.plot(x,y,'r',ls="--")
ax.plot(x_LT4,y_LT4,'b')
# Edit some settings
ax.axvline(x=0,color="k",ls=":")
ax.axhline(y=0,color="k",ls=":")
ax.grid(True)
ax.axis([-2,4,-1,2])
ax.set_aspect('equal')
ax.set_title("Shear");
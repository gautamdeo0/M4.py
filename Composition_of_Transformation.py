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
theta = pi/6
C = np.array([[sin(theta),-cos(theta)],[-cos(theta),-sin(theta)]])
C_coords = C@coords
x_LT5 = C_coords[0,:]
y_LT5 = C_coords[-1,:]
# Create the figure and axes objects
fig, ax = plt.subplots()
# Plot the points. x and y are original vectors, x_LT1 and y_LT1 are images
ax.plot(x,y,'ro')
ax.plot(x_LT5,y_LT5,'bo')
# Connect the points by lines
ax.plot(x,y,'r',ls="--")
ax.plot(x_LT5,y_LT5,'b')
# Edit some settings
ax.axvline(x=0,color="k",ls=":")
ax.axhline(y=0,color="k",ls=":")
ax.grid(True)
ax.axis([-1.5,1.5,-1.5,1.6])
ax.set_aspect('equal');
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#make axis
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

#lenght of x axis between (-2, 7.25)
xv = np.linspace(-2, 0)
xz = np.linspace(0, 3)
xc = np.linspace(3, 7.16606)
#np.meshgrid() #an addition to 3d figure

#1st function: f(x) = -1/4x +0.1*sin(3x)+2 , -2;0
function1 = plt.plot(xv, -1/4*xv+0.1*np.sin(3*xv)+2)
#2nd function: g(x) = -1/3x+0.1*sin(3x)+2 , 0;3
function2 = plt.plot(xz, -1/3*xz+0.1*np.sin(3*xz)+2)
#3rd function: h(x)= -1/4x +0.05*cos(3x)+1.83556 , 3;7.16606
function3 = plt.plot(xc, -1/4*xc +0.05*np.cos(3*xc)+1.83556)

#labels
plt.xlabel('x-akse')
plt.ylabel('y-akse')
plt.title("Rummelige figurer")

#plt.axis('tight')

#display
plt.show()

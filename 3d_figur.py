import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D #register use of 3D projection
import scipy.integrate as integrate

#import Tkinter

#make axis
fig = plt.figure()
#ax = fig.add_subplot(1,1,1, projection='3d')
ax = fig.gca(projection='3d')

#2D plots:
#lenght of x axis between (-2, 7.16606)
xv = np.linspace(-2, 0)
xz = np.linspace(0, 3)
xc = np.linspace(3, 7.16606)

#1st function: f(x) = -1/4x +0.1*sin(3x)+2 , -2;0
function1 = plt.plot(xv, -1/4*xv+0.1*np.sin(3*xv)+2)
#2nd function: g(x) = -1/3x+0.1*sin(3x)+2 , 0;3
function2 = plt.plot(xz, -1/3*xz+0.1*np.sin(3*xz)+2)
#3rd function: h(x) = -1/4x +0.05*cos(3x)+1.83556 , 3;7.16606
function3 = plt.plot(xc, -1/4*xc +0.05*np.cos(3*xc)+1.83556)

'''
#3D plots:
xxv = np.linspace(-2, 0)
yxv = (integrate.quad(lambda x: (((-1)/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
xxxv, yyxv = np.meshgrid(xxv, yxv, sparse=True)

#zxv = (integrate.quad(lambda x: (((-1)/4*x+0.1*np.sin(3*x)+2)**2), -2, 0))
ax.plot_trisurf(xxv, yxv, z, linewidth=0.2, antialiased=True)
#h = plt.contourf(xxv, yxv, resultzz) #cannot use 2D Array
'''

print("Integration")
#1st function
#resultz = Axes3D.plot(xv, yv, integrate.quad((((-1)/4*xv+0.1*np.sin(3*xv)+2)**2), -2, 0))
resultz = integrate.quad(lambda x: (((-1)/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
resultzz = np.pi * resultz[0]
print("1. function:", resultzz)
#2nd function
resultx = integrate.quad(lambda x: (((-1)/3*x+0.1*np.sin(3*x)+2)**2), 0, 3)
resultxx = np.pi * resultx[0]
print("2. function:", resultxx)
#3rd function
resultc = integrate.quad(lambda x: (((-1)/4*x+0.5*np.cos(3*x)+1.83556)**2), 3, 7.16606)
resultcc = np.pi * resultc[0]
print("3. function:", resultcc)


#labels
plt.xlabel('x-akse')
plt.ylabel('y-akse')
plt.title("Rummelige figur")

#display
plt.show()

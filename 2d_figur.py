import matplotlib.pyplot as plt
import numpy as np

#lenght of x axis between (-2, 7.25)
xv = np.linspace(-2, 0)
xz = np.linspace(0, 3)
xc = np.linspace(3, 7.16606)
#np.meshgrid() #an addition to 3d figure

'''
def f1(t):
    return (-1/4*x + 0.1 * np.sin(3*x ) + 2)
t1 = np.arange(-2.0,0.0)
plt.plot(f1(t1))

def f2(t):
    return (-1/3*x+0.1*np.sin(3*x)+2)
t2 = np.arange(0.0,3.0)
plt.plot(f2(t2))

def f3(t):
    return (-1/4*x +0.05*np.cos(3*x)+1.83556)
t3 = np.arange(3.0,7.16606)
plt.plot(f3(t3))
'''

#1st function: f(x) = -1/4x +0.1*sin(3x)+2 , -2;0
function1 = plt.plot(xv, -1/4*xv+0.1*np.sin(3*xv)+2)
#2nd function: g(x) = -1/3x+0.1*sin(3x)+2 , 0;3
function2 = plt.plot(xz, -1/3*xz+0.1*np.sin(3*xz)+2)
#3rd function: h(x)= -1/4x +0.05*cos(3x)+1.83556 , 3;7.16606
function3 = plt.plot(xc, -1/4*xc +0.05*np.cos(3*xc)+1.83556)

#labels
plt.xlabel('x-akse')
plt.ylabel('y-akse')

plt.axis('tight')

#display
plt.show()

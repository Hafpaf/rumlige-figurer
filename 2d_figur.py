import matplotlib.pylab as plt
import numpy as np
x = np.linspace(-np.pi, np.pi, 201)
#plt.plot(x, np.sin(x))

#1st function: f(x) = -1/4x +0.1*sin(3x)+2 , -2;0
plt.plot(x, (-1/4*x + 0.1 * np.sin(3*x ) + 2))
#2nd function: g(x) = -1/3x+0.1*sin(3x)+2 , 0;3
plt.plot(x, -1/3*x+0.1*np.sin(3*x)+2)
#3rd function: h(x)= -1/4x +0.05*cos(3x)+1.83556
plt.plot(x, -1/4*x +0.05*np.cos(3*x)+1.83556)

#labels
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')

plt.axis('tight')
plt.show() #display

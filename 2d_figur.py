import matplotlib.pylab as plt
import numpy as np
x = np.linspace(-np.pi, np.pi, 201)
#plt.plot(x, np.sin(x))
plt.plot(x, (-1/4*x + 0.1 * np.sin(3*x ) + 2))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

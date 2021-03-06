import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#make axis
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

#sinus function
Fs = 8000
f = 5
sample = 10
x = np.arange(sample)
#y = np.sin(2 * np.pi * f * x / Fs)

y = (-1/4*x + 0.1 * np.sin(3*x ) + 2)

#plt.xlabel("x-akse")
#plt.ylabel("y-akse")
#plt.zlabel("z-akse")
plt.title("Rummelige figurer")

plt.show() #starts the visual projector

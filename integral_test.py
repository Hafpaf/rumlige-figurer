import scipy.integrate as integrate
import scipy.special as special
import numpy as np

#result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
#print(result)

#1st function
resultz = integrate.quad(lambda x: (((-1)/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
#print(resultz)
for result in resultz:
    if result > 0.0:
        print("1: ", result)
#2nd function
resultx = integrate.quad(lambda x: (((-1)/3*x+0.1*np.sin(3*x)+2)**2), 0, 3)
for result in resultx:
    if result > 0.0:
        print("2: ", result)
#3rd function
resultc = integrate.quad(lambda x: (((-1)/4*x+0.5*np.cos(3*x)+1.83556)**2), 3, 7.16606)
for result in resultc:
    if result in resultc:
        if result > 0.0:
            print("3 :", result)

'''

#funktion
def function():
    resultz = integrate.quad(lambda x: ((-1/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
    Fz = np.pi*resultz
    return Fz
print(function())
'''

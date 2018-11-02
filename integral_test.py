import scipy.integrate as integrate
import scipy.special as special
import numpy as np

#result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
#print(result)

resultz = integrate.quad(lambda x: ((-1/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
print(resultz)
for result in resultz:
    if result > 0.1:
        print(result)
#funktion
#F(x)=integrate.quad(((-1/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
'''
#funktion
def function1():
    resultz = integrate.quad(lambda x: ((-1/4*x+0.1*np.sin(3*x)+2)**2), -2, 0)
    Fz = np.pi*resultz
    return Fz
print(function1())
'''

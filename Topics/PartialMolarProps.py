# fit of mixture property and determination of moalr and partial molar values

import numpy as np
from scipy.optimize import curve_fit
import pylab as plt
from sympy import *

def f(x,a,b,c):
    # fit function with y = f(x,p) with parameters p = (a,b,c)
    return a+b*x+c*x**2

def f_vpm1(a,b,c):
    # function for determination of partial molar 1
    y = Symbol('y')
    return a+b*y+c*y**2+ diff(a+b*y+c*y**2,y)*(1-y)

def f_vpm2(a,b,c):
    #function for determination of partial molar 2
    y = Symbol('y')
    return a+b*y+c*y**2- diff(a+b*y+c*y**2,y)*(y)

# data
xData = np.linspace(0.2,0.8,7)
vmData = np.array([0.119,0.116,0.112,0.109,0.107,0.107,0.11])

#call curve fit function to get best values of a, b, c
popt,pcov = curve_fit(f,xData,vmData)
a,b,c = popt
print ("Optimal parameters are a=%g, b=%g, and c=%g" %(a,b,c))
x = np.linspace(0,1,100)

#determining the molar and partial molar values
vfitted = f(x,*popt)#equivalent to f(x,popt[0],popt[1],popt[2])
vm1 = vfitted[0]
vm2 = vfitted[99]
y = Symbol('y')
lam_f_vpm1 = lambdify(y,f_vpm1(a,b,c))
vpm1 = lam_f_vpm1(x)
lam_f_vpm2 = lambdify(y,f_vpm2(a,b,c))
vpm2 = lam_f_vpm2(x)

print("The molar volume of species 1 = %g cm3/mol" %vm1)
print("The molar volume of species 2 = %g cm3/mol" %vm2)
print("The partial molar volume of species 1 = %g cm3/mol" %vpm1[4])

#plotting
plt.plot(xData,vmData,'o',label='data$vm$')
plt.plot(x,vfitted,'-',label='fit$f(x_i)$')
plt.plot(x,vpm1,'r--',label='vpm1')
plt.plot(x,vpm2,'b--',label='vpm2')
plt.xlim(0,1)
plt.xlabel('x')
plt.legend()
plt.show()



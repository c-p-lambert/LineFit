import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("Marshmallow_data.csv", delimiter=",", dtype=str)
x = data[1:,0].astype(np.float32)
y = data[1:,1].astype(np.float32)
print("y=",y)
print("x=", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
print(slope)
print(intercept)
###EXERCISE 1
print_equation(slope,intercept,"g","cm")
#The equation of the line is: y = -0.004549450640794716 cm/g x + 5.900000053810218 cm
##EXERCISE 2
plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(slope, x, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("mass(g)") #change the units as appropriate
plt.ylabel("height(cm)")  #change the units as appropriate
plt.show()

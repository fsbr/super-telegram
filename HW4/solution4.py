import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(-10,10,1000)
F1 = (2/w**3)*( 10*w*np.cos(5*w) + (25*w**2 -2)*np.sin(5*w) )
Fa1 = np.abs(F1) 
plt.plot(w,Fa1)
plt.show()

# problem 2
a = 2
F2L = np.sin(4*np.pi*(a-w))/(a-w)
F2R = np.sin(4*np.pi*(a+w))/(a+w)
F2 = np.abs(F2L + F2R)
plt.plot(w,F2)
plt.show()

# problem 3
# to test this, i just change the 4 to an 8, i dont re derive the 
# entire window function
a = 2
F2L = np.sin(8*np.pi*(a-w))/(a-w)
F2R = np.sin(8*np.pi*(a+w))/(a+w)
F2 = np.abs(F2L + F2R)
plt.plot(w,F2)
plt.show()



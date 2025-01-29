import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,8,0.1)
U = 10
G = 6.6743 * (10**-11)
r = 1000
M = 5.9722 * (10**24)
def radio_function(U,t):
    dmdt = (G*M)/(U*(r**2))
    return dmdt

U_t = odeint(radio_function, U, t)

plt.plot(t, U_t[:,0])
plt.savefig("fig_5.png")
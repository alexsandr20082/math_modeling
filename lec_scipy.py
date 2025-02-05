import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,10**6,100)

def radio_function(m,t):
    dmdt = -k * m
    return dmdt

m_0 = 10
k = 1.61 * 10 **(-6)
	
m_t = odeint(radio_function, m_0, t)

plt.plot(t, m_t[:,0], label='распад Висмута 210')
plt.savefig("fig_1.png")
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
t = np.linspace(0, 100, 1000)
def move_func(y, t): 
    A, B, C = y
    dA_dt = -k1 * A
    dB_dt = k1 * A - k2 * B
    dC_dt = k2 * B - k3 * C
    return dA_dt, dB_dt, dC_dt
    
k1 = 1  
k2 = 0.5
k3 = 0.2
A0 = 10 
B0 = 0   
C0 = 0
y0 = [A0, B0, C0]

sol = odeint(move_func, y0, t)
plt.plot(t,sol[:,0])
plt.plot(t,sol[:,1])
plt.plot(t,sol[:,2])
plt.savefig("pig.png")

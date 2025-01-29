import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5,5,0.01)

def diff_func(v,t):
    y,t  = w
    dy_dt = v 
    dv_dt = -4*v - 5*y
    return dy_dt, dv_dt

y0 = 4
dy0_dt = -1
w = y0,dy0_dt


sol = odeint(diff_func,w,t)


	
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.savefig('fig_6.png')
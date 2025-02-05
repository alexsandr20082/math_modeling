import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1,1,0.01)

def diff_func(w,t):
    y, x, z = w

    dx_dt = 3*x-y+z
    dy_dt = x+y+z
    dz_dt = 4*x-y+4*z
    return dy_dt, dy_dt, dz_dt

x0 = -71
y0 = 1
z0 = -3
w0 = y0, y0, z0


sol = odeint(diff_func,w0,t)


	
plt.plot(t, sol[:, 0], 'b', label='theta(t)')

plt.plot(t, sol[:, 1], 'r', label='theta(t)')


plt.savefig('fig_7.png')


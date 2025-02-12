import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 100, 1000)
def move_func(y, t): 
    A, X, Y = y
    dA_dt = - (k1 + k2) * A
    dX_dt = k1 * A
    dY_dt = k2 * A
    return dA_dt, dX_dt,dY_dt

k1 = 0.1  
k2 = 0.05  
A0 = 10.0
y0 = [A0, 0.0, 0.0]

sol = odeint(move_func, y0, t)
A = sol[:, 0]
X = sol[:, 1]
Y = sol[:, 2]

fig, ax = plt.subplots()
 
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')	
 
def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
 
edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
	
ani.save('animation_4.gif', writer="pillow")
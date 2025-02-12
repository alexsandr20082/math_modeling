import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
t = np.linspace(0, 100, 1000)
def move_func(y, t): 
    x, v = y
    f_t = 5 * np.cos(w * t)  
    dxdt = v
    dvdt = -k/m * x - 0.8/m * v + f_t/m 
    return [dxdt, dvdt]
m = 0.5  
d_L = 0.08  
F0 = 1.0 
w = 2 * np.pi

k = F0 / d_L  

v0 = 0.5  
x0 = -d_L
y0 = [x0, v0]

sol = odeint(move_func, y0, t)
x = sol[:, 0]
v = sol[:, 1]

fig, ax = plt.subplots()
 
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')	
 
def animate(i):
    ball.set_data([0], [sol[i][0]])
    # ball_line.set_data(sol[:i, 0], sol[:i, 1])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
 
edge = 1
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('animation_9.gif', writer="pillow")
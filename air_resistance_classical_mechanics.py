import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.optimize import root_scalar
import math as m

g = 9.81
k_small = 1e-6
k_current = k_small
v0 = 600
theta = m.pi / 3
U = v0 * m.cos(theta)
V = v0 * m.sin(theta)

k_list = [k_small, 0.01, 0.02, 0.04, 0.08, 0.005]


def x(t, k):
    return (U / k) * (1 - np.exp(-k * t))

def y(t, k):
    return (-g * t) / k + ((k * V + g) / (k * k)) * (1 - np.exp(-k * t))

def x_k(t):
    return x(t, k_current)

def y_k(t):
    return y(t, k_current)


plt.axes().set_aspect('equal', 'datalim')
fig, ax = plt.subplots()

T = [None] * len(k_list)
paths = []

for i, k_n in enumerate(k_list):
    l_obj = ax.plot([], [], lw=2)[0]
    l_obj.set_data([], [])
    paths.append(l_obj)


for i, k_n in enumerate(k_list):
    k_current = k_n
    sol = root_scalar(y_k, bracket=[0.1, 200], method='brentq')
    T[i] = sol.root
    t_list = np.arange(0, T[i], 0.1)
    paths[i] = ax.plot(x_k(t_list), y_k(t_list))

def init():
    for path in paths:
        path[0].set_data([], [])
    return paths

def animate(dt):
    t_current = dt * 0.36
    for i, k_n in enumerate(k_list):
        if t_current < T[i]:
            t_list = np.arange(0, t_current, 0.1)
            paths[i][0].set_data(x(t_list, k_n), y(t_list, k_n))
    return paths


ax.set(xlabel='x-position (m)', ylabel='y-position (m)', title='Shots fired.')
ax.grid()
ax.axes.set_aspect('equal')

anim = animation.FuncAnimation(
    fig, animate, frames=334, interval=40, blit=False)

fig.savefig("test.png")

writer_gif = animation.PillowWriter(fps=50)
anim.save("drag_coefficients_flight_simulation.gif", writer=writer_gif)
plt.draw()
plt.show()
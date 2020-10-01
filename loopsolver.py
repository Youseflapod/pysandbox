import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math as m


def radius_for_height(height, init_velocity, gravity, accel_const):
    return (init_velocity ** 2 - 2 * np.abs(gravity) * height) / accel_const;


def draw_arc(x_start,y_start,radius,theta_start,dt_theta,theta_step):
    # theta_start = m.atan((x_start-x) / (y_start-y));
    theta_array = np.linspace(theta_start, theta_start + dt_theta, int(round(dt_theta/theta_step)))
    x = radius * m.cos(theta_start + m.pi) + x_start
    y = radius * m.sin(theta_start + m.pi) + y_start
    x_array = radius * np.cos(theta_array) + x
    y_array = radius * np.sin(theta_array) + y
    theta_end = theta_start + dt_theta
    x_end = x_array[-1]
    y_end = y_array[-1]
    return x_array, y_array, x_end, y_end, theta_end


print("Hello World!")

# Data for plotting
# t = np.arange(-1, 1, 0.01)
# t = np.linspace(-1, 1, 100)
# s = np.sqrt(1 - t ** 2)

circ_test = draw_arc(0.0, 0.0, 3, -m.pi / 2, m.pi / 2, 0.1)
circ_test2 = draw_arc(3, 3, 1, 0, 2, 0.1)


plt.axes().set_aspect('equal', 'datalim')
fig, ax = plt.subplots()
# ax.plot(circ_test[0], circ_test[1])
# ax.plot(circ_test2[0], circ_test2[1])

theta_current = -m.pi / 2
THETA_STEP = 0.0001
NUM_OF_SECTIONS = 10000
DT_THETA = (2*m.pi) / NUM_OF_SECTIONS
x_current = 0.0
y_current = 0.0

INIT_VELOCITY = 15 * 0.44704
G = -9.81
ACCEL_CONST = -G * 3.5
x_array = np.array([0])
y_array = np.array([0])

while theta_current <= m.pi * (1.499 + 2):
    radius = radius_for_height(y_current, INIT_VELOCITY, G, ACCEL_CONST)
    arc = draw_arc(x_current, y_current, radius, theta_current, DT_THETA, THETA_STEP)
    # ax.plot(arc[0], arc[1])
    x_array = np.append(x_array, arc[0])
    y_array = np.append(y_array, arc[1])
    x_current = arc[2]
    y_current = arc[3]
    theta_current = arc[4]
    # print("R: %.3f  x_end: %.3f  y_end %.3f" %(radius, x_current, y_current))

ax.plot(x_array, y_array)

ax.set(xlabel='x-position (m)', ylabel='y-position (m)',
       title='About as simple as it gets, folks')
ax.grid()
ax.axes.set_aspect('equal')

fig.savefig("test.png")
plt.show()



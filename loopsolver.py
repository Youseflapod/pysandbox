import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math as m

print("Hello World!")

# Data for plotting
# t = np.arange(-1, 1, 0.01)
t = np.linspace(-1, 1, 100)
s = np.sqrt(1 - t ** 2)

plt.axes().set_aspect('equal', 'datalim')
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
ax.axes.set_aspect('equal')

fig.savefig("test.png")
plt.show()


def radius_for_height(height, init_velocity, gravity, accel_const):
    return (init_velocity ** 2 - 2 * np.abs(gravity) * height) / accel_const;

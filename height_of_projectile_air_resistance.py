import numpy as np
import pandas
import xlrd
import math as m

v_initial = 6000;
g_initial = 9.81
radius_earth = 6.371e6
G = 6.674e-11
M = 5.972e24
mass = 2000
radius = 0.5
area = radius ** 2 * m.pi
drag_coefficient = 0.2

air_density = pandas.read_excel('data_air_density_altitude_meters.xlsx', header=None)


def delta_v(delta_y, v_0, k, g):
    y = delta_y
    v_f = m.sqrt((m.exp(-2 * k * y) * (k * (v_0 ** 2) + g) - g) / k)
    return v_f - v_0


def k_of_density(density):
    return (1 / (2 * mass)) * drag_coefficient * density * area


def g_of_height(h, initial_radius):
    return (G * M) / (initial_radius + h) ** 2


v_curr = v_initial
y_curr = 0
print(len(air_density))
print(air_density[0][1])

for i in range(0, len(air_density) - 2):
    d_y = air_density[0][i + 1] - air_density[0][i]
    g_curr = g_of_height(y_curr, radius_earth)
    y_curr = y_curr + d_y
    density_curr = air_density[1][i]
    k_curr = k_of_density(density_curr)
    d_v = delta_v(d_y, v_curr, k_curr, g_curr)
    v_curr = v_curr + d_v
    print(v_curr, y_curr, d_v, d_y, k_curr, g_curr)


R = y_curr + radius_earth
remaining_altitude = 1 / ((1 / R) - (v_curr ** 2) / (2 * G * M)) - R
print(remaining_altitude)
print("Final Altitude: ", (remaining_altitude + y_curr))

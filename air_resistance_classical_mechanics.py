import matplotlib.pyplot as plt
import numpy as np
import math as m

g=9.81
k=0.00000001
v0 = 600
theta = m.pi/3
U = v0 * m.cos(theta)
V = v0 * m.sin(theta)

def x(t):
    return (U/k)*(1-m.exp())
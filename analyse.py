#!/usr/bin python3
# _*_ coding: utf-8 _*_
import cmath as cm
import numpy as np
from matplotlib import pyplot as plt

# define useful constant.
ev = 1.6e-19        # electron volt
U0 = 0.5 * ev       # barrier height
m = 9e-31           # mass of electron
h = 6.626e-34       # Plank constant
h_ = h / (2 * np.pi)# h bar
# a = 0.16            # barrier width


def K1(ratio):
    ratio = 0.01 if ratio < 0.01 else ratio if ratio != 1 else ratio + 1e-10
    scale = 0.5e-8 / cm.sqrt(ratio)
    return scale * cm.sqrt(2 * m * ratio*U0 / np.square(h_))


def K2(ratio):
    ratio = 0.01 if ratio < 0.01 else ratio if ratio != 1 else ratio + 1e-10
    scale = 0.5e-8 / cm.sqrt(ratio)
    return scale * cm.sqrt(2 * m * (ratio * U0 - U0) / np.square(h_))


def D(k1, k2, a):
    return 4 * np.square(k1 * k2) / (
        np.square((np.square(k1) - np.square(k2)) * np.sin(k2 * a)) + 4 * np.square(k1 * k2))


def R(d):
    return 1 - d

# a = 0.16
# ratio = np.linspace(0, 10, 100)
# d = [D(K1(r), K2(r), a) for r in ratio]
# plt.title('Relationship With Energy of Wave')
# plt.hold(True)
# plt.plot(ratio, np.real(d), 'r', label='translation ratio')
# plt.plot(ratio, np.real([R(d_) for d_ in d]), 'b', label='reflection ratio')
# plt.legend()
# plt.show()

ratio = 1
a = np.linspace(1e-10, 1, 100)
d = [D(K1(ratio), K2(ratio), a_) for a_ in a]
plt.title('Relationship With Barrier Width')
plt.hold(True)
plt.plot(a, np.real(d), 'r', label='translation ratio')
plt.plot(a, np.real([R(d_) for d_ in d]), 'b', label='reflection ratio')
plt.legend()
plt.show()

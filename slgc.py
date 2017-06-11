#!/usr/bin python3
# _*_ coding: utf-8 _*_
import os
import im2gif
import cmath as cm
import numpy as np
from io import BytesIO
from PIL import Image as im
from matplotlib import pyplot as plt

# define useful constant.
ev = 1.6e-19        # electron volt
U0 = 0.5 * ev       # barrier height
m = 9e-31           # mass of electron
h = 6.626e-34       # Plank constant
h_ = h / (2 * np.pi)# h bar
a = 0.16            # barrier width

# set ratio of E/U0
ratio = float(input('please input ratio of E/U0: '))
# ratio = 1
# to avoid ratio being smaller than 0.01 or equal to 1
ratio = 0.01 if ratio < 0.01 else ratio if ratio != 1 else ratio + 1e-10

# define wave Energy E
E = ratio * U0

# set scale value.(it can contral the wave number in a given area)
# while scale = 0.5e-8, there are no auto scale
# if you don't want auto scale, just del denominator: cm.sqrt(ratio)
scale = 0.5e-8 / cm.sqrt(ratio)

# define wave vactor k
k1 = scale * cm.sqrt(2 * m * E / pow(h_, 2))        # wave factor of part 1 and 3
k2 = scale * cm.sqrt(2 * m * (E - U0) / pow(h_, 2)) # wave factor of part 2

# define intensity ratio of wave
# A and A_ belong to wave of part 1
# B and B_ belong to wave of part 2
# C and C_ belong to wave of part 3
# De is just a common denominator value
# we define A = 1 and others will be directly proportional to A
A = 1
De = pow(k1 - k2, 2) * np.exp(1j * k2 * a) - pow(k1 + k2, 2) * np.exp(-1j * k2 * a)
A_ = 2j * (pow(k1, 2) - pow(k2, 2)) * np.sin(a * k2) * A / De
C = -4 * k1 * k2 * np.exp(-1j * k1 * a) * A / De
B = (A * k1 + A * k2 - A_ * k1 + A_ * k2) / (2 * k2)
B_ = (A * k2 - A * k1 + A_ * k1 + A_ * k2)/ (2 * k2)

# define three part
x1 = np.linspace(-1, 0, 10e3)       # x limit of part 1
x2 = np.linspace(0, a, 10e3)        # x limit of part 2
x3 = np.linspace(a, a + 1, 10e3)    # x limit of part 3

# define wave function
y1_r = A * np.exp(1j * k1 * x1)     # right wave function of part 1
y1_l = A_ * np.exp(-1j * k1 * x1)   # left wave function of part 1
y2_r = B * np.exp(1j * k2 * x2)     # right wave function of part 2
y2_l = B_ * np.exp(-1j * k2 * x2)   # left wave function of part 2
y3_r = C * np.exp(1j * k1 * x3)     # right wave function of part 3

y1 = y1_r + y1_l                    # wave function of part 1
y2 = y2_r + y2_l                    # wave function of part 2
y3 = y3_r                           # wave function of part 3

# debug out
# print('k1', k1, '\nk2', k2, '\nA', A, '\nA_', A_, '\nB', B, '\nB_', B_, '\nC', C, '\nDe', De)

# create a new figure
plt.figure(figsize=(10,45/8))

# set axis scope
plt.axis([-1, a + 1, -4, 4])

# hide the axis
plt.axis('off')

# set hold on
plt.hold(True)

# draw wave in part 1 and get three plot handle for data updating later
h10, = plt.plot(x1, np.real(y1), 'g-', label='composite wave', linewidth=2)
h11, = plt.plot(x1, np.real(y1_r), 'g--', label='incident wave', linewidth=2)
h12, = plt.plot(x1, np.real(y1_l), 'r--', label='reflected wave', linewidth=2)

# draw legend
plt.legend(fontsize=14, frameon=True, fancybox=True, framealpha=0.3)

# draw wave in part 2 and get three plot handle for data updating later
h20, = plt.plot(x2, np.real(y2), 'g-', linewidth=2)
h21, = plt.plot(x2, np.real(y2_r), 'b--', linewidth=2)
h22, = plt.plot(x2, np.real(y2_l), 'r--', linewidth=2)

# draw wave in part 3
h30, = plt.plot(x3, np.real(y3), 'g-', linewidth=2)

# draw barrier line
plt.plot([-1,0,0,a,a,a+1], [-3,-3,3,3,-3,-3], 'k-', linewidth=2)

# draw reference center line
plt.plot([-1, a + 1], [0, 0], color='gray', linestyle='-.')

# set hold off
plt.hold(False)

# draw text information
## define font dict creater function
def font(family='serif', color='black', weight='normal', size='16'):
    return {'family': family, 'color': color, 'weight': weight, 'size': size}
## draw title
plt.title('Barrier Penetration And Tunneling', fontdict=font(size=20))
## draw barrier height value U0
plt.text(a, 3, '$U_0$', fontdict=font(size=20))
## draw value of E/U0
plt.text(-.8, 3, '$\itE/\itU_0=\it%.2f$' % ratio, fontdict=font(size=20))
## draw barrier left limit
plt.text(-.02, -3.3, '$0$', fontdict=font())
## draw barrier right limit
plt.text(a-.02, -3.3, '$a$', fontdict=font())
## draw x axis mark 'x'
plt.text(a+.95, -2.95, '$x$', fontdict=font())
## draw water mark of author
plt.text(a+.7, -3.4, '$author: ph$', fontdict=font(color='gray'))
# show plot
# plt.show()

# set gif save root dir
gif_root = './gif'
# check gif root dir
if not os.path.isdir(gif_root):
    os.makedirs(gif_root)
# set frame number N
FN = 40
# pre storage allocation
images = []
for i in range(FN):
    # add time factor
    Et = np.exp(-2j * np.pi * i / FN)

    # update the plot data
    h10.set_ydata(np.real(y1 * Et))
    h11.set_ydata(np.real(y1_r * Et))
    h12.set_ydata(np.real(y1_l * Et))
    h20.set_ydata(np.real(y2 * Et))
    h21.set_ydata(np.real(y2_r * Et))
    h22.set_ydata(np.real(y2_l * Et))
    h30.set_ydata(np.real(y3 * Et))

    # create bytes buffer
    buf = BytesIO()

    # save plot date to buf
    plt.savefig(buf, format='png')

    # read buf as image date and append to images 
    images.append(im.open(buf))
# set gif file save path
gif_path = os.path.join(gif_root, 'slgc_%.2f.gif' % ratio)
# create GIF dynamic plot from images
im2gif.writeGif(filename=gif_path, images=images, duration=2 / FN)

# print status message
print('gif file created at path: %s.' % os.path.abspath(gif_path))

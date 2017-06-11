import os
import im2gif
import cmath as cm
from io import BytesIO
import numpy as np
from PIL import Image as im
from matplotlib import pyplot as plt

a = 0.6
b = 0.3
k0 = 20
# set ratio of E/U0
ratio = float(input('please input ratio of E/U0: '))
# ratio = 1
# to avoid ratio being smaller than 0.01 or equal to 1
ratio = 0.01 if ratio < 0.01 else ratio if ratio != 1 else ratio + 1e-10

scale = 1 / cm.sqrt(ratio)

k1 = scale*k0*cm.sqrt(ratio)
k2 = scale*k0*cm.sqrt(ratio - 1)


A1 = 1
A2 = A1*(-2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) + k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    + k1**4*np.exp(2.0*1j*a*k1) + 2.0*k1**4*np.exp(2.0*1j*b*k2) - k1**4*np.exp(4.0*1j*b*k2) 
    - k1**4 + 2.0*k1**3*k2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - 2.0*k1**3*k2*np.exp(2.0*1j*a*k1) 
    + 2.0*k1**3*k2*np.exp(4.0*1j*b*k2) - 2.0*k1**3*k2 - 2.0*k1*k2**3*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    + 2.0*k1*k2**3*np.exp(2.0*1j*a*k1) - 2.0*k1*k2**3*np.exp(4.0*1j*b*k2) + 2.0*k1*k2**3 
    + 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) - k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    - k2**4*np.exp(2.0*1j*a*k1) - 2.0*k2**4*np.exp(2.0*1j*b*k2) + k2**4*np.exp(4.0*1j*b*k2) 
    + k2**4)*np.exp(-2.0*1j*b*k1)/(-2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k1**4*np.exp(2.0*1j*a*k1) 
    + 2.0*k1**4*np.exp(2.0*1j*b*k2) - k1**4*np.exp(4.0*1j*b*k2) - k1**4 
    + 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) - 4.0*k1**3*k2 + 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) 
    - 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) - 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) - 6.0*k1**2*k2**2 
    + 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) - 4.0*k1*k2**3 - 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k2**4*np.exp(2.0*1j*a*k1) + 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    - k2**4*np.exp(4.0*1j*b*k2) - k2**4)
B1 = 2.0*A1*k1*(k1**3*np.exp(2.0*1j*(a*k1 + b*k2)) - k1**3*np.exp(2.0*1j*a*k1) - k1**3*np.exp(2.0*1j*b*k2) 
    + k1**3 - k1**2*k2*np.exp(2.0*1j*(a*k1 + b*k2)) + k1**2*k2*np.exp(2.0*1j*a*k1) + k1**2*k2*np.exp(2.0*1j*b*k2) 
    + 3.0*k1**2*k2 - k1*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) + k1*k2**2*np.exp(2.0*1j*a*k1) 
    + k1*k2**2*np.exp(2.0*1j*b*k2) + 3.0*k1*k2**2 + k2**3*np.exp(2.0*1j*(a*k1 + b*k2)) - k2**3*np.exp(2.0*1j*a*k1) 
    - k2**3*np.exp(2.0*1j*b*k2) + k2**3)*np.exp(-1j*b*(k1 - k2))/(2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - k1**4*np.exp(2.0*1j*a*k1) - 2.0*k1**4*np.exp(2.0*1j*b*k2) 
    + k1**4*np.exp(4.0*1j*b*k2) + k1**4 - 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) + 4.0*k1**3*k2 
    - 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) + 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    + 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) + 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) + 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) 
    + 6.0*k1**2*k2**2 - 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) + 4.0*k1*k2**3 + 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - k2**4*np.exp(2.0*1j*a*k1) - 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    + k2**4*np.exp(4.0*1j*b*k2) + k2**4)
B2 = 2.0*A1*k1*(k1**3*np.exp(2.0*1j*(a*k1 + b*k2)) - k1**3*np.exp(2.0*1j*a*k1) - k1**3*np.exp(2.0*1j*b*k2) 
    + k1**3 + k1**2*k2*np.exp(2.0*1j*(a*k1 + b*k2)) - k1**2*k2*np.exp(2.0*1j*a*k1) + 3.0*k1**2*k2*np.exp(2.0*1j*b*k2) 
    + k1**2*k2 - k1*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) + k1*k2**2*np.exp(2.0*1j*a*k1) - 3.0*k1*k2**2*np.exp(2.0*1j*b*k2) 
    - k1*k2**2 - k2**3*np.exp(2.0*1j*(a*k1 + b*k2)) + k2**3*np.exp(2.0*1j*a*k1) + k2**3*np.exp(2.0*1j*b*k2) 
    - k2**3)*np.exp(1j*b*(-k1 + k2))/(-2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) + k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    + k1**4*np.exp(2.0*1j*a*k1) + 2.0*k1**4*np.exp(2.0*1j*b*k2) - k1**4*np.exp(4.0*1j*b*k2) - k1**4 
    + 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) - 4.0*k1**3*k2 + 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) 
    - 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) - 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) - 6.0*k1**2*k2**2 
    + 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) - 4.0*k1*k2**3 - 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k2**4*np.exp(2.0*1j*a*k1) + 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    - k2**4*np.exp(4.0*1j*b*k2) - k2**4)
C1 = 4.0*A1*k1*k2*(k1**2*np.exp(2.0*1j*b*k2) - k1**2 - 2.0*k1*k2*np.exp(2.0*1j*b*k2) - 2.0*k1*k2 
    + k2**2*np.exp(2.0*1j*b*k2) - k2**2)*np.exp(1j*b*(-k1 + k2))/(-2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k1**4*np.exp(2.0*1j*a*k1) + 2.0*k1**4*np.exp(2.0*1j*b*k2) 
    - k1**4*np.exp(4.0*1j*b*k2) - k1**4 + 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) - 4.0*k1**3*k2 
    + 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) - 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    - 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) - 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) - 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) 
    - 6.0*k1**2*k2**2 + 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) - 4.0*k1*k2**3 - 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k2**4*np.exp(2.0*1j*a*k1) + 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    - k2**4*np.exp(4.0*1j*b*k2) - k2**4)
C2 = 4.0*A1*k1*k2*(k1**2*np.exp(2.0*1j*b*k2) - k1**2 - k2**2*np.exp(2.0*1j*b*k2) 
    + k2**2)*np.exp(1j*(2.0*a*k1 - b*k1 + b*k2))/(-2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k1**4*np.exp(2.0*1j*a*k1) + 2.0*k1**4*np.exp(2.0*1j*b*k2) 
    - k1**4*np.exp(4.0*1j*b*k2) - k1**4 + 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) - 4.0*k1**3*k2 
    + 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) - 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    - 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) - 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) - 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) 
    - 6.0*k1**2*k2**2 + 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) - 4.0*k1*k2**3 - 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k2**4*np.exp(2.0*1j*a*k1) + 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    - k2**4*np.exp(4.0*1j*b*k2) - k2**4)
D1 = 8.0*A1*k1**2*k2*(k1 + k2)*np.exp(1j*(a*k1 - a*k2 - b*k1 + b*k2))/(2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - k1**4*np.exp(2.0*1j*a*k1) - 2.0*k1**4*np.exp(2.0*1j*b*k2) 
    + k1**4*np.exp(4.0*1j*b*k2) + k1**4 - 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) + 4.0*k1**3*k2 
    - 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) + 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    + 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) + 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) + 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) 
    + 6.0*k1**2*k2**2 - 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) + 4.0*k1*k2**3 + 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - k2**4*np.exp(2.0*1j*a*k1) - 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    + k2**4*np.exp(4.0*1j*b*k2) + k2**4)
D2 = 8.0*A1*k1**2*k2*(k1 - k2)*np.exp(1j*(a*k1 + a*k2 - b*k1 + 3.0*b*k2))/(-2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k1**4*np.exp(2.0*1j*a*k1) + 2.0*k1**4*np.exp(2.0*1j*b*k2) 
    - k1**4*np.exp(4.0*1j*b*k2) - k1**4 + 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) - 4.0*k1**3*k2 
    + 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) - 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    - 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) - 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) - 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) 
    - 6.0*k1**2*k2**2 + 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) - 4.0*k1*k2**3 - 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    + k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) + k2**4*np.exp(2.0*1j*a*k1) + 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    - k2**4*np.exp(4.0*1j*b*k2) - k2**4)
E1 = 16.0*A1*k1**2*k2**2*np.exp(-2.0*1j*b*(k1 - k2))/(2.0*k1**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - k1**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - k1**4*np.exp(2.0*1j*a*k1) - 2.0*k1**4*np.exp(2.0*1j*b*k2) 
    + k1**4*np.exp(4.0*1j*b*k2) + k1**4 - 4.0*k1**3*k2*np.exp(4.0*1j*b*k2) + 4.0*k1**3*k2 
    - 4.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + b*k2)) + 2.0*k1**2*k2**2*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) 
    + 2.0*k1**2*k2**2*np.exp(2.0*1j*a*k1) + 4.0*k1**2*k2**2*np.exp(2.0*1j*b*k2) + 6.0*k1**2*k2**2*np.exp(4.0*1j*b*k2) 
    + 6.0*k1**2*k2**2 - 4.0*k1*k2**3*np.exp(4.0*1j*b*k2) + 4.0*k1*k2**3 + 2.0*k2**4*np.exp(2.0*1j*(a*k1 + b*k2)) 
    - k2**4*np.exp(2.0*1j*(a*k1 + 2.0*b*k2)) - k2**4*np.exp(2.0*1j*a*k1) - 2.0*k2**4*np.exp(2.0*1j*b*k2) 
    + k2**4*np.exp(4.0*1j*b*k2) + k2**4)


x1 = np.linspace(-1-b,-b,100)
x2 = np.linspace(-b,0,100)
x3 = np.linspace(0,a,100)
x4 = np.linspace(a,a+b,100)
x5 = np.linspace(a+b,a+b+1,100)

y1_r = A1*np.exp(1j*k1*x1)
y1_l = A2*np.exp(-1j*k1*x1)
y2_r = B1*np.exp(1j*k2*x2)
y2_l = B2*np.exp(-1j*k2*x2)
y3_r = C1*np.exp(1j*k1*x3)
y3_l = C2*np.exp(-1j*k1*x3)
y4_r = D1*np.exp(1j*k2*x4)
y4_l = D2*np.exp(-1j*k2*x4)
y5_r = E1*np.exp(1j*k1*x5)

y1 = y1_r + y1_l
y2 = y2_r + y2_l
y3 = y3_r + y3_l
y4 = y4_r + y4_l
y5 = y5_r


plt.figure(figsize=(10,45/8))
plt.axis([-1-b, a + b + 1, -4, 4])
# hide the axis
plt.axis('off')
plt.hold(True)
h1, = plt.plot(x1, np.real(y1))
h2, = plt.plot(x2, np.real(y2))
h3, = plt.plot(x3, np.real(y3))
h4, = plt.plot(x4, np.real(y4))
h5, = plt.plot(x5, np.real(y5))
# draw barrier line
plt.plot([-1-b,-b,-b,0,0,a,a,a+b,a+b,a+b+1], [-3,-3,3,3,-3,-3,3,3,-3,-3], 'k-', linewidth=2)
# draw reference center line
plt.plot([-1-b, a+b + 1], [0, 0], color='gray', linestyle='-.')
plt.hold(False)

# plt.show()

# set gif save root dir
gif_root = './gif2'
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
    h1.set_ydata(np.real(y1 * Et))
    h2.set_ydata(np.real(y2 * Et))
    h3.set_ydata(np.real(y3 * Et))
    h4.set_ydata(np.real(y4 * Et))
    h5.set_ydata(np.real(y5 * Et))


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

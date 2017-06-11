import os
import im2gif
import cmath as cm
import numpy as np
from io import BytesIO
from PIL import Image as im
from matplotlib import pyplot as plt

def font(family='serif', color='black', weight='normal', size='16'):
    return {'family': family, 'color': color, 'weight': weight, 'size': size}

# relationship with ratio
# ratio = np.linspace(0,5,1e4)
# ratio[ratio==1]=1+1e-10
# k0 = 1e-10
# k1 = np.array([k0*cm.sqrt(r) for r in ratio])
# k2 = np.array([k0*cm.sqrt(r-1) for r in ratio])
# D = 4*np.square(k1)*np.square(k2)/(np.square(np.square(k1)-np.square(k2))*np.square(np.sin(k2))+4*np.square(k1)*np.square(k2))
# R = 1-D
# flg = plt.figure(figsize=(10,45/8))
# plt.xlabel('$E/U_0$', fontdict=font())
# plt.ylabel('$Intensity$', fontdict=font())
# plt.title('Relationship With $E/U_0$')
# plt.hold(True)
# hd, = plt.plot(ratio, np.real(D), color='blue', label='transmission coefficient')
# hr, = plt.plot(ratio, np.real(R), color='red', label='reflection coefficient')
# plt.legend(fontsize=14, frameon=True, fancybox=True, framealpha=0.3)
# plt.hold(False)
# ht= plt.text(2.1,.5,'$k_0=%.2f$' % k0, fontdict=font(size=20))
# # plt.show()
# gif_root = './gif'
# # check gif root dir
# if not os.path.isdir(gif_root):
#     os.makedirs(gif_root)
# FN = 50
# images = []
# for k0 in np.linspace(0,50,FN):
#     k1 = np.array([k0*cm.sqrt(r) for r in ratio])
#     k2 = np.array([k0*cm.sqrt(r-1) for r in ratio])

#     D = 4*np.square(k1)*np.square(k2)/(np.square(np.square(k1)-np.square(k2))*np.square(np.sin(k2))+4*np.square(k1)*np.square(k2))
#     R = 1-D

#     hd.set_ydata(np.real(D))
#     hr.set_ydata(np.real(R))
#     ht.set_text('$k_0=%.2f$' % k0)
#     buf = BytesIO()
#     plt.savefig(buf, format='png')
#     images.append(im.open(buf))
# gif_path = os.path.join(gif_root, 'analyse_r2e.gif' % ratio)
# im2gif.writeGif(filename=gif_path, images=images, duration=2 / FN)
# print('gif file created at path: %s.' % os.path.abspath(gif_path))

# relationship with k0
ratio = 0.01
ratio = 0.01 if ratio < 0.01 else ratio if ratio != 1 else ratio + 1e-10
k0 = np.linspace(0,20,1e3)

k1 = k0*cm.sqrt(ratio)
k2 = k0*cm.sqrt(ratio-1)

D = 4*np.square(k1)*np.square(k2)/(np.square(np.square(k1)-np.square(k2))*np.square(np.sin(k2))+4*np.square(k1)*np.square(k2))
R = 1-D

flg = plt.figure(figsize=(10,45/8))
plt.xlabel('$k_0$', fontdict=font())
plt.ylabel('$Intensity$', fontdict=font())
plt.title('Relationship With $K0$')
plt.hold(True)
hd, = plt.plot(k0, np.real(D), color='blue', label='transmission coefficient')
hr, = plt.plot(k0, np.real(R), color='red', label='reflection coefficient')
plt.legend(fontsize=14, frameon=True, fancybox=True, framealpha=0.3)
plt.hold(False)
ht = plt.text(8,.5,'$E/U_0=%.2f$' % ratio, fontdict=font(size=20))
# plt.show()
gif_root = './gif'
# check gif root dir
if not os.path.isdir(gif_root):
    os.makedirs(gif_root)
FN = 40
images = []
for ratio in np.linspace(0,5,FN):
    k1 = k0*cm.sqrt(ratio)
    k2 = k0*cm.sqrt(ratio-1)

    D = 4*np.square(k1)*np.square(k2)/(np.square(np.square(k1)-np.square(k2))*np.square(np.sin(k2))+4*np.square(k1)*np.square(k2))
    R = 1-D

    hd.set_ydata(np.real(D))
    hr.set_ydata(np.real(R))
    ht.set_text('$E/U_0=%.2f$' % ratio)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    images.append(im.open(buf))
gif_path = os.path.join(gif_root, 'analyse_e2r.gif' % ratio)
im2gif.writeGif(filename=gif_path, images=images, duration=2 / FN)
print('gif file created at path: %s.' % os.path.abspath(gif_path))
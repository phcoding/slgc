import cmath as cm
import numpy as np
from matplotlib import pyplot as plt

def font(family='serif', color='black', weight='normal', size='16'):
    return {'family': family, 'color': color, 'weight': weight, 'size': size}

# ratio = np.linspace(0,5,1e4)
# ratio[ratio==1]=1+1e-10

# k0 = 10
# k1 = np.array([k0*cm.sqrt(r) for r in ratio])
# k2 = np.array([k0*cm.sqrt(r-1) for r in ratio])

# D = 4*np.square(k1)*np.square(k2)/(np.square(np.square(k1)-np.square(k2))*np.square(np.sin(k2))+4*np.square(k1)*np.square(k2))
# R = 1-D

# flg = plt.figure(figsize=(10,45/8))
# plt.xlabel('$E/U_0$', fontdict=font())
# plt.ylabel('$Intensity$', fontdict=font())
# plt.title('Relationship With $E/U_0$')
# plt.hold(True)
# plt.plot(ratio, np.real(D), color='blue', label='transmission coefficient')
# plt.plot(ratio, np.real(R), color='red', label='reflection coefficient')
# plt.legend(fontsize=14, frameon=True, fancybox=True, framealpha=0.3)
# plt.hold(False)
# plt.text(2.1,.5,'$k_0=%.2f$' % k0, fontdict=font(size=20))
# plt.show()

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
plt.plot(k0, np.real(D), color='blue', label='transmission coefficient')
plt.plot(k0, np.real(R), color='red', label='reflection coefficient')
plt.legend(fontsize=14, frameon=True, fancybox=True, framealpha=0.3)
# plt.hold(False)
plt.text(8,.5,'$E/U_0=%.2f$' % ratio, fontdict=font(size=20))
plt.show()
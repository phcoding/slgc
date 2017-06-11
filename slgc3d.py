import cmath
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm  
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
a = 10
k0 = 1
ratio = 0.9

k0 = 1
k1 = k0*cmath.sqrt(ratio)
k2 = k0*cmath.sqrt(ratio-1)
A1 = 1
De = (k1-k2)**2*np.exp(1j*k2*a)-(k1+k2)**2*np.exp(-1j*k2*a)
A2 = 2*1j*(k1**2-k2**2)*np.sin(a*k2)*A1/De;
C = -4*k1*k2*np.exp(-1j*k1*a)*A1/De;
B1 = (A1*k1+A1*k2-A2*k1+A2*k2)/(2*k2);
B2 = A1+A2-B1;

sr = 20
r1 = np.linspace(0, 16, sr)
r2 = np.linspace(16, 16+a, sr)
r3 = np.linspace(16+a, 44, sr)
q = np.linspace(0, 2*np.pi, sr)
rh1, qh1 = np.meshgrid(r1, q)
rh2, qh2 = np.meshgrid(r2, q)
rh3, qh3 = np.meshgrid(r3, q)
x1 = rh1*np.cos(qh1)
x2 = rh2*np.cos(qh2)
x3 = rh3*np.cos(qh3)
y1 = rh1*np.sin(qh1)
y2 = rh2*np.sin(qh2)
y3 = rh3*np.sin(qh3)
z1 = A1*np.exp(1j*k1*(rh1-16)) + A2*np.exp(-1j*k1*(rh1-16))
z2 = B1*np.exp(1j*k2*(rh2-16)) + B2*np.exp(-1j*k2*(rh2-16))
z3 = C*np.exp(1j*k1*(rh3-16))

fig = plt.figure(figsize=(10,45/8))
ax = Axes3D(fig)
plt.axis([-44,44,-44,44])
#plt.axis('off')
ax.set_zlim(-3,3)
plt.hold(True)

h1 = ax.plot_surface(x1,y1,np.real(z1), rstride=1, cstride=1, cmap=cm.coolwarm,  
        linewidth=0, antialiased=False);
h2 = ax.plot_surface(x2,y2,np.real(z2), rstride=1, cstride=1, cmap=cm.coolwarm,  
        linewidth=0, antialiased=False);
h3 = ax.plot_surface(x3,y3,np.real(z3), rstride=1, cstride=1, cmap=cm.coolwarm,  
        linewidth=0, antialiased=False);
plt.hold(False)
#ax.set_zlim(-1.01, 1.01)  
#ax.zaxis.set_major_locator(LinearLocator(10))  
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  
#fig.colorbar(h1, shrink=0.5, aspect=5)  
plt.show()

FN = 40
images = []
for i in range(FN):
    Et = np.exp(-1j*2*np.pi*i/FN)
    #h1.scatter(np.real(z1*Et))
    #h2.scatter(np.real(z2*Et))
    #h3.scatter(np.real(z3*Et))

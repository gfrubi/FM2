import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
plt.style.use('classic')

th,ph = np.meshgrid(np.linspace(0,np.pi,200),np.linspace(0,2*np.pi,200)) #arrays de variables angulares

def X(R):
    return R*np.sin(th)*np.cos(ph)

def Y(R):
    return R*np.sin(th)*np.sin(ph)

def Z(R):
    return R*np.cos(th)

nmax = 5

fig = plt.figure(figsize=(3*nmax,3*nmax))
for n in range(nmax+1):
    for m in range(n+1):
        print(n,m)
        ax = fig.add_subplot(nmax+1, nmax+1, (nmax+1)*n+1+m, projection='3d')
        f = sp.sph_harm_y(n, m, th, ph).real # evalúa la parte real del armónico esférico
        norm = colors.Normalize()
        ax.plot_surface(X(1),Y(1),Z(1),rstride=1, cstride=1,norm=norm,cmap=cm.jet,facecolors=cm.jet(norm(f)))
        ax.set_title('$n = %d, m= %d$'%(n,m), fontsize=20)
        ax.set_axis_off()
        colores = cm.ScalarMappable(cmap=cm.jet)
        colores.set_array(f)
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        ax.set_zlim(-1,1)
        ax.set_box_aspect((1, 1, 1))
plt.subplots_adjust(wspace=0, hspace=0)
fig.tight_layout()
#fig.show()
fig.savefig('../figs/fig-Aes3Dcolores.png', dpi=100)
#fig.savefig('../figs/fig-Aes3Dcolores.pdf')

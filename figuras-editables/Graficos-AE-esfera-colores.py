import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
#style.use('classic')
plt.rc('text', usetex=True)

t,p = np.meshgrid(np.linspace(0,np.pi,200),np.linspace(0,2*np.pi,200)) #arrays de variables angulares

def X(R):
    return R*np.sin(t)*np.cos(p)

def Y(R):
    return R*np.sin(t)*np.sin(p)

def Z(R):
    return R*np.cos(t)

nmax = 5

fig = plt.figure(figsize=(3*nmax,3*nmax))
for n in range(nmax+1):
    for m in range(n+1):
        #print(n,m)
        ax = fig.add_subplot(nmax+1, nmax+1, (nmax+1)*n+1+m, projection='3d')
        C = sp.sph_harm(m, n, p, t).real
        norm = colors.Normalize()
        ax.plot_surface(X(1),Y(1),Z(1),rstride=1, cstride=1,norm=norm,cmap=cm.jet,facecolors=cm.jet(norm(C)))
        ax.set_title('$n = %d, m= %d$'%(n,m), fontsize=20)
        #ax.set_frame_on(False)
        ax.set_axis_off()
        cosa = cm.ScalarMappable(cmap=cm.jet)
        cosa.set_array(C)
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        ax.set_zlim(-1,1)
plt.subplots_adjust(wspace=0, hspace=0)
fig.tight_layout()
#fig.show()
fig.savefig('../figs/fig-Aes3Dcolores.png', dpi=100)
#fig.savefig('../figs/fig-Aes3Dcolores.pdf')

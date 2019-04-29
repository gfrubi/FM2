# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import numpy as np
plt.style.use('classic')

def Psi_k(k,x,y):
    term_psi = (8/np.pi**3)*(np.sin((2.*k-1.)*np.pi*x)/(2*k-1)**3)*(np.sinh((2*k-1)*np.pi*y)/np.sinh(2*np.pi*(2*k-1)))
    return term_psi

def SnPsi(n,x,y):
    SnPsi = 0
    for k in range(1,n+1):
        SnPsi += Psi_k(k,x,y)
    return SnPsi

x = np.linspace(0,1,200) # Definiendo el dominio en x
y = np.linspace(0,2,200) # Definiendo el dominio en y
X,Y = np.meshgrid(x, y) # Formando la grilla x,y
m = 30 # número máximo en el que se cortará la serie
Z = SnPsi(m,X,Y) # Evaluando el valor del potencial


#A continuación, un gráfico en colores en el dominio.
plt.pcolormesh(X, Y, Z)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$y$',fontsize=15)
plt.title('$\psi(x,y)$',fontsize=15)
plt.colorbar()
plt.show()
#savefig('fig-MSV-rectangulo-color.pdf')


# Y ahora un gráfico de superficie y en colores.

fig = plt.figure(figsize=(8,6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, rstride=5, cstride=5, alpha=1)
fig.colorbar(surf, shrink=0.6, aspect=8) #Se agrega barra de colores
ax.set_xlabel('$x$',fontsize=15)
ax.set_ylabel('$y$',fontsize=15)
ax.set_zlabel('$\psi(x,y)$',fontsize=15)
plt.show()
#savefig('../figs/fig-MSV-rectangulo-3D.pdf')

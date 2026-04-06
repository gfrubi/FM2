import matplotlib.pyplot as plt
import numpy as np
plt.style.use('bmh')

def Psi_k(k,x,y):
    term_psi = (8/np.pi**3)*(np.sin((2*k-1.)*np.pi*x)/(2*k-1)**3)*(np.sinh((2*k-1)*np.pi*y)/np.sinh(2*np.pi*(2*k-1)))
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
fig = plt.figure(figsize=(8,6))
plt.pcolormesh(X, Y, Z, cmap='plasma')
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$y$',fontsize=15)
plt.title('$\\psi(x,y)$',fontsize=15)
plt.colorbar(aspect=40)
plt.grid(False)
#plt.savefig('../figs/fig-MSV-rectangulo-color.pdf')
plt.show()



# Y ahora un gráfico de superficie y en colores.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', rstride=5, cstride=5, alpha=1)
fig.colorbar(surf, shrink=0.6, aspect=40) #Se agrega barra de colores
ax.view_init(14,-116)
ax.set_xlabel('$x$',fontsize=15)
ax.set_ylabel('$y$',fontsize=15)
ax.set_zlabel('$\\psi(x,y)$',fontsize=15)
ax.set_yticks([0,0.5,1,1.5,2])
#plt.savefig('../figs/fig-MSV-rectangulo-3D.pdf')
plt.show()

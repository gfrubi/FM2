import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, yn, kv, iv, spherical_jn, spherical_yn, spherical_in, spherical_kn
plt.style.use('bmh')

colores = ['blue','red','brown','purple','black']
dasheses = [[],[5,2],[5,5],[5,2,2,2],[2,2]]

x = np.linspace(-10,10,1000)

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,jn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$J_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#plt.title('Funciones de Bessel de $1^{a}$ especie y orden entero')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Bessel-J.pdf')

# $N_{\nu}(x)$

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,yn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$Y_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#plt.title('Funciones de Bessel de $2^{da}$ especie y orden entero')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Bessel-Y.pdf')


# $I_{\nu}(z)$

x = np.linspace(-4,4,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,iv(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$I_n(x)$',fontsize=15)
#plt.title('Funciones modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=13)
plt.legend(loc='best',fontsize=12)
plt.xlim(-4,4)
plt.ylim(-10,12)
plt.savefig('../figs/fig-Bessel-I.pdf')


# $K_{\nu}(z)$

x = np.linspace(0,4,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,kv(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$K_n(x)$',fontsize=15)
#plt.title('Funciones modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=13)
plt.legend(loc='best',fontsize=12)
plt.ylim(0,4)
plt.savefig('../figs/fig-Bessel-K.pdf')


# #$j_{n}(x)$:

x = np.linspace(0,10,1000)

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,spherical_jn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$j_n(x)$',fontsize=15)
#plt.title('Funciones Esféricas de Bessel de $1^{\\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.ylim(-0.5,1.1)
plt.savefig('../figs/fig-Bessel-Esferica-j.pdf')


# #$n_{n}(x)$:

x = np.linspace(-20,20,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,spherical_yn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$y_n(x)$',fontsize=15)
#plt.title('Funciones Esféricas de Bessel de $2^{\\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.ylim(-1,1)
plt.savefig('../figs/fig-Bessel-Esferica-y.pdf')


# #$i_{n}(x)$:

x = np.linspace(0,5,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,spherical_in(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$i_n(x)$',fontsize=15)
#plt.title('Funciones Esféricas Modificadas de Bessel de $1^{\text{a}}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Bessel-Esferica-i.pdf')


# #$k_{n}(x)$:


x = np.linspace(5,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,spherical_kn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$k_n(x)$',fontsize=15)
#plt.title('Funciones Esféricas Modificadas de Bessel de $2^{\text{da}}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.ylim(-1,15)

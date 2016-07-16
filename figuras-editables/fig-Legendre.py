# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *

colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

x=np.linspace(-1,1,500)


# #$P_n(x)$
fig = plt.figure(figsize=(8,6),dpi=500)
for n in range(5):
    plt.plot(x,legendre(n)(x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$P_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#plt.title(r'Polinomios de Legendre')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Legendre-P.pdf')


# P'_n(x)
def der_pol_legendre(n,z):
    return lpn(n,z)[1][n]
der_pol_legendre=np.vectorize(der_pol_legendre)

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,der_pol_legendre(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$P^{\prime}_n(x)$',fontsize=15)
plt.ylim(-10.1,10.1)
#plt.title(r'Derivadas de Polinomios de Legendre')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Legendre-der-P.pdf')


# Q_n(x)
def Q_legendre(n,z):
    return lqn(n,z)[0][n]
Q_legendre=np.vectorize(Q_legendre)

x=np.linspace(-1,1,100)
nm=4
fig = plt.figure(figsize=(8,6),dpi=500)
for n in range(nm+1):
    plt.plot(x,Q_legendre(n,x), colores[n], dashes=dasheses[n],label=r'$Q_{%d}(x)$'%n, linewidth=2)
#plt.title(ur'Funciones de Legendre de segunda especie')
plt.legend(loc='best',fontsize=11)
plt.grid()
plt.ylim(-2,2)
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$Q_n(x)$',fontsize=15)
plt.savefig('../figs/fig-Legendre-Q.pdf')


# #$P_{l}^{m}(x)$

def asoc_legendre(m,n,z):
    return lpmn(m,n,z)[0][m][n]
asoc_legendre = np.vectorize(asoc_legendre)

fig = plt.figure(figsize=(8,6),dpi=500)
l=1
for m in range(-l,l+1):
    plt.plot(x,asoc_legendre(-m,l,x),colores[m], dashes=dasheses[m], linewidth=2,label=r'$P^{%d}_{%d}(x)$'%(m,l))
#plt.title(ur'Funciones asociadas de Legendre: $l=%d$'%l)
plt.xlabel(r'$x$', fontsize=15)
plt.ylabel(r'$P^{m}_{%d}(x)$'%l, fontsize=15)
plt.legend(loc='best',fontsize=12)
plt.grid()
plt.savefig('../figs/fig-Legendre-Asoc-l-%d.pdf'%l)


fig = plt.figure(figsize=(8,6),dpi=500)
l=2
for m in range(-l,l+1):
    plt.plot(x,asoc_legendre(-m,l,x),colores[m], dashes=dasheses[m], linewidth=2,label=r'$P^{%d}_{%d}(x)$'%(m,l))
#plt.title(ur'Funciones asociadas de Legendre: $l=%d$'%l)
plt.xlabel(r'$x$', fontsize=15)
plt.ylabel(r'$P^{m}_{%d}(x)$'%l, fontsize=15)
plt.legend(loc='best',fontsize=12)
plt.grid()
plt.savefig('../figs/fig-Legendre-Asoc-l-%d.pdf'%l)


fig = plt.figure(figsize=(8,6),dpi=500)
l=3
for m in range(-l,l+1):
    plt.plot(x,asoc_legendre(-m,l,x),colores[m], dashes=dasheses[m], linewidth=2,label=r'$P^{%d}_{%d}(x)$'%(m,l))
#plt.title(ur'Funciones asociadas de Legendre: $l=%d$'%l)
plt.xlabel(r'$x$', fontsize=15)
plt.ylabel(r'$P^{m}_{%d}(x)$'%l, fontsize=15)
plt.legend(loc='best',fontsize=12)
plt.grid()
plt.savefig('../figs/fig-Legendre-Asoc-l-%d.pdf'%l)


# #$Q_{l}(x)$

def Q_legendre(n,z):
    return lqn(n,z)[0][n]
Q_legendre=np.vectorize(Q_legendre)

fig = plt.figure(figsize=(8,6),dpi=500)
for n in range(5):
    plt.plot(x,Q_legendre(n,x),colores[n], dashes=dasheses[n], linewidth=2,label='$n= $'+str(n))
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$Q_n(x)$',fontsize=15)
plt.ylim(-2.1,2.1)
#plt.title(ur'Funciones de Legendre de segunda especie')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Legendre-Q.pdf')



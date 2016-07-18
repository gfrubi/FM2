# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *

colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

x = np.linspace(-10,10,1000)

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,jn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$J_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#plt.title(r'Funciones de Bessel de $1^{\circ}$ especie a orden entero')
plt.legend(loc='best',fontsize=12)
plt.ylim(-0.7,1.1)
plt.savefig('../figs/fig-Bessel-J.pdf')

# $N_{\nu}(x)$

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,yn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$N_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#plt.title(r'Funciones de Bessel de $2^{\circ}$ especie a orden entero')
plt.legend(loc='best',fontsize=12)
plt.ylim(-2,0.7)
plt.savefig('../figs/fig-Bessel-N.pdf')


# $I_{\nu}(z)$

x = np.linspace(-4,4,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,iv(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$I_n(x)$',fontsize=15)
#plt.title(r'Funciones modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=13)
plt.legend(loc='best',fontsize=12)
plt.xlim(-4,4)
plt.ylim(-10,12)
plt.savefig('../figs/fig-Bessel-I.pdf')


# $K_{\nu}(z)$

x = np.linspace(0,4,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,kv(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$K_n(x)$',fontsize=15)
#plt.title(r'Funciones modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=13)
plt.legend(loc='best',fontsize=12)
plt.ylim(0,4)
plt.savefig('../figs/fig-Bessel-K.pdf')


# #$j_{n}(x)$:

def fun_sph_jn(n,z):
    return sph_jn(n,z)[0][n]
fun_sph_jn= np.vectorize(fun_sph_jn)

x = np.linspace(-10,10,1000)

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,fun_sph_jn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$j_n(x)$',fontsize=15)
#plt.title(ur'Funciones Esféricas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.ylim(-0.5,1.1)
plt.savefig('../figs/fig-Bessel-Esferica-j.pdf')


# #$n_{n}(x)$:

def fun_sph_yn(n,z):
    return sph_yn(n,z)[0][n]
fun_sph_yn= np.vectorize(fun_sph_yn)

x = np.linspace(-20,20,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,fun_sph_yn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$n_n(x)$',fontsize=15)
#plt.title(ur'Funciones Esféricas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.ylim(-1,1)
plt.savefig('../figs/fig-Bessel-Esferica-n.pdf')


# #$i_{n}(x)$:

def fun_sph_in(n,z):
    return sph_in(n,z)[0][n]
fun_sph_in= np.vectorize(fun_sph_in)

x = np.linspace(-5,5,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,fun_sph_in(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$i_n(x)$',fontsize=15)
#plt.title(ur'Funciones Esféricas Modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.xlim(-5,5)
plt.ylim(-10,10)
plt.savefig('../figs/fig-Bessel-Esferica-i.pdf')


# #$k_{n}(x)$:

def fun_sph_kn(n,z):
    return sph_kn(n,z)[0][n]
fun_sph_kn= np.vectorize(fun_sph_kn)

x = np.linspace(-5,5,1000)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,fun_sph_kn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$k_n(x)$',fontsize=15)
#plt.title(ur'Funciones Esféricas Modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12)
plt.xlim(-5,5)
plt.ylim(-15,15)
plt.savefig('../figs/fig-Bessel-Esferica-k.pdf')


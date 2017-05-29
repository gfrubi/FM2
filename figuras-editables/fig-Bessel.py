# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.special import *

style.use('classic')

colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

x = linspace(-10,10,1000)

fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,jn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$J_n(x)$',fontsize=15)
ylim(-1.1,1.1)
#title(r'Funciones de Bessel de $1^{\circ}$ especie a orden entero')
legend(loc='best',fontsize=12)
ylim(-0.7,1.1)
savefig('../figs/fig-Bessel-J.pdf')

# $N_{\nu}(x)$

fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,yn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$N_n(x)$',fontsize=15)
ylim(-1.1,1.1)
#title(r'Funciones de Bessel de $2^{\circ}$ especie a orden entero')
legend(loc='best',fontsize=12)
ylim(-2,0.7)
savefig('../figs/fig-Bessel-N.pdf')


# $I_{\nu}(z)$

x = linspace(-4,4,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,iv(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$I_n(x)$',fontsize=15)
#title(r'Funciones modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=13)
legend(loc='best',fontsize=12)
xlim(-4,4)
ylim(-10,12)
savefig('../figs/fig-Bessel-I.pdf')


# $K_{\nu}(z)$

x = linspace(0,4,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,kv(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$K_n(x)$',fontsize=15)
#title(r'Funciones modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=13)
legend(loc='best',fontsize=12)
ylim(0,4)
savefig('../figs/fig-Bessel-K.pdf')


# #$j_{n}(x)$:

def fun_sph_jn(n,z):
    return sph_jn(n,z)[0][n]
fun_sph_jn= vectorize(fun_sph_jn)

x = linspace(-10,10,1000)

fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,fun_sph_jn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$j_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
legend(loc='best',fontsize=12)
ylim(-0.5,1.1)
savefig('../figs/fig-Bessel-Esferica-j.pdf')


# #$n_{n}(x)$:

def fun_sph_yn(n,z):
    return sph_yn(n,z)[0][n]
fun_sph_yn= vectorize(fun_sph_yn)

x = linspace(-20,20,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,fun_sph_yn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$n_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=12)
legend(loc='best',fontsize=12)
ylim(-1,1)
savefig('../figs/fig-Bessel-Esferica-n.pdf')


# #$i_{n}(x)$:

def fun_sph_in(n,z):
    return sph_in(n,z)[0][n]
fun_sph_in= vectorize(fun_sph_in)

x = linspace(-5,5,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,fun_sph_in(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$i_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas Modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
legend(loc='best',fontsize=12)
xlim(-5,5)
ylim(-10,10)
savefig('../figs/fig-Bessel-Esferica-i.pdf')


# #$k_{n}(x)$:

def fun_sph_kn(n,z):
    return sph_kn(n,z)[0][n]
fun_sph_kn= vectorize(fun_sph_kn)

x = linspace(-5,5,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,fun_sph_kn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$k_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas Modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=12)
legend(loc='best',fontsize=12)
xlim(-5,5)
ylim(-15,15)

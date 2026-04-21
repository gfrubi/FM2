import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")
from scipy.special import legendre_p, lqn, assoc_legendre_p # ver https://docs.scipy.org/doc/scipy/reference/special.html#legendre-functions

colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

x = np.linspace(-1,1,500)

# $P_n(x)$
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,legendre_p(n,x)[0],colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$P_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#plt.title('Polinomios de Legendre')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Legendre-P.pdf')


# P'_n(x)
fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,legendre_p(n,x,diff_n=1)[-1],colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
plt.grid(True)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$P^{\\prime}_n(x)$',fontsize=15)
plt.ylim(-10.1,10.1)
#plt.title('Derivadas de Polinomios de Legendre')
plt.legend(loc='best',fontsize=12)
plt.savefig('../figs/fig-Legendre-der-P.pdf')


# Q_n(x)
def Q_legendre(n,z):
    return lqn(n,z)[0][n]
Q_legendre=np.vectorize(Q_legendre)

fig = plt.figure(figsize=(8,6))
for n in range(5):
    plt.plot(x,Q_legendre(n,x), colores[n], dashes=dasheses[n],label='$Q_{%d}(x)$'%n, linewidth=2)
#plt.title(ur'Funciones de Legendre de segunda especie')
plt.legend(loc='best',fontsize=11)
plt.grid(True)
plt.ylim(-2,2)
plt.xlabel('$x$',fontsize=15)
plt.ylabel('$Q_n(x)$',fontsize=15)
plt.savefig('../figs/fig-Legendre-Q.pdf')


# #$P_{l}^{m}(x)$
for l in range(1,4):
    fig = plt.figure(figsize=(8,6))
    for m in range(-l,l+1):
        plt.plot(x,assoc_legendre_p(l,m,x)[0],colores[m], dashes=dasheses[m], linewidth=2,label='$P^{%d}_{%d}(x)$'%(m,l))
    #plt.title('Funciones asociadas de Legendre: $l=%d$'%l)
    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$P^{m}_{%d}(x)$'%l, fontsize=15)
    plt.legend(loc='best')
    plt.grid(True)
    plt.savefig('../figs/fig-Legendre-Asoc-l-%d.pdf'%l)




# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def sn_delta(n,x,T):
    """
    Implementación escalar de la serie truncada hasta orden $n$ de la serie de Fourier de la función delta de dirac con período $T$.
    """    
    sn_delta = np.ones(len(x))/T
    for k in range(1,n+1):
        sn_delta += (2/T)*np.cos((2*np.pi*k*x)/T)
    return sn_delta

T = 2*np.pi
t = np.linspace(-3*np.pi,3*np.pi,1000)
n = 4
fig = plt.figure(figsize=(15,5))
plt.xticks([-3*np.pi,-2*np.pi,-np.pi,0,np.pi,2*np.pi,3*np.pi],['$-3T/2$','$-T$','$-T/2$','$0$','$T/2$','$T$','$3T/2$'])
colores = ['blue','red','brown','purple']
dasheses = [[],[8,2],[6,6],[8,2,2,2]]
for k in range(n):
    plt.plot(t,sn_delta(k,t,T),colores[k], dashes=dasheses[k],label=r"$S_{%d}(t)$" % k,lw=2)
plt.yticks([-1./T,0,1./T,3./T,5/T,7/T],['$-1/T$','$0$','$1/T$','$3/T$','$5/T$','$7/T$'])
plt.xlabel(r'$t$',fontsize=15)
plt.ylabel(r'$S_n(t)$',fontsize=15)
plt.legend(loc='best',fontsize=13)
plt.grid()
fig.savefig("../figs/fig-Fourier-serie-Dirac.pdf")

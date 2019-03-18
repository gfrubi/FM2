# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def sn_signo(m,x):
    """
    Implementación escalar de la serie truncada hasta orden m de la serie de Fourier de la función signo.
    """    
    sn_signo = 0
    for k in range(m+1):
        sn_signo += (4/np.pi)*np.sin((2*k+1)*x)/(2.*k+1.)
    return sn_signo

x = np.linspace(-3.*np.pi,3.*np.pi,300)
x_signo = np.linspace(-np.pi,np.pi,100)

fig = plt.figure(figsize=(15,5))
plt.plot(x_signo,np.sign(x_signo),'black',label=r'$f(\theta)$',lw=3)
colores = ['blue','red','brown','purple']
dasheses = [[],[8,2],[6,6],[8,2,2,2]]
for k in range(4):
    plt.plot(x,sn_signo(k,x),colores[k], dashes=dasheses[k],label=r"$S_{%d}(\theta)$" % k,lw=2)
#plt.title(ur'Serie de Fourier de Función Signo truncada hasta $n=%d$'% n,fontsize=18)
plt.yticks([-1,0,1],['-1','0','1'])
plt.xticks([-3*np.pi,-2*np.pi,-np.pi,0,np.pi,2*np.pi,3*np.pi],['$-3\pi$','$-2\pi$','$-\pi$','0','$\pi$','$2\pi$','$3\pi$'])
plt.xlabel(r'$\theta$',fontsize=15)
plt.ylabel(r'$S_n(\theta)$',fontsize=15)
plt.legend(loc='best', fontsize=13)
plt.grid()
fig.savefig("../figs/fig-Fourier-serie-signo.pdf")

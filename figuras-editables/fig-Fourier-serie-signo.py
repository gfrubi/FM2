# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *

def sn_signo(m,x):
    """
    Implementación escalar de la serie truncada hasta orden n de la serie de Fourier de la función signo.
    """    
    sn_signo=0
    for k in range(m+1):
        sn_signo=sn_signo+(4/pi)*sin((2*k+1)*x)/(2.*k+1.)
    return sn_signo

x=linspace(-3.*pi,3.*pi,300)
x_signo=linspace(-pi,pi,100)

fig=figure(figsize=(15,5))
plot(x_signo,sign(x_signo),'black',label=r'$f(\theta)$',lw=3)
colores=['blue','red','brown','purple']
dasheses=[[],[8,2],[6,6],[8,2,2,2]]
for k in range(4):
    plot(x,sn_signo(k,x),colores[k], dashes=dasheses[k],label=r"$S_{%d}(\theta)$" % k,lw=2)
#title(ur'Serie de Fourier de Función Signo truncada hasta $n=%d$'% n,fontsize=18)
yticks([-1,0,1],['-1','0','1'])
xticks([-3*pi,-2*pi,-pi,0,pi,2*pi,3*pi],['$-3\pi$','$-2\pi$','$-\pi$','0','$\pi$','$2\pi$','$3\pi$'])
xlabel(r'$\theta$',fontsize=15)
ylabel(r'$S_n(\theta)$',fontsize=15)
legend(loc='best', fontsize=13)
grid()
fig.savefig("../figs/fig-Fourier-serie-signo.pdf")

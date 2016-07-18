# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *

def sn_delta(m,x,T):
    """
    Implementación escalar de la serie truncada hasta orden $n$ de la serie de Fourier de la función delta de dirac con período $T$.
    """    
    sn_delta=ones(len(x))/T
    for k in range(1,m+1):
        sn_delta=sn_delta + (2/T)*cos((2*pi*k*x)/T)
    return sn_delta

T=2*pi
t=linspace(-3*pi,3*pi,1000)
n=4
fig=figure(figsize=(15,5))
xticks([-3*pi,-2*pi,-pi,0,pi,2*pi,3*pi],['$-3T/2$','$-T$','$-T/2$','$0$','$T/2$','$T$','$3T/2$'])
colores=['blue','red','brown','purple']
dasheses=[[],[8,2],[6,6],[8,2,2,2]]
for k in range(n):
    plot(t,sn_delta(k,t,T),colores[k], dashes=dasheses[k],label=r"$S_{%d}(t)$" % k,lw=2)
yticks([-1./T,0,1./T,3./T,5/T,7/T],['$-1/T$','$0$','$1/T$','$3/T$','$5/T$','$7/T$'])
xlabel(r'$t$',fontsize=15)
ylabel(r'$S_n(t)$',fontsize=15)
legend(loc='best',fontsize=13)
grid()
fig.savefig("../figs/fig-Fourier-serie-Dirac.pdf")

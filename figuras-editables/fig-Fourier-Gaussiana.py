# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *

x=linspace(-10,10,1000)
k=linspace(-10,10,1000)
alpha=1
fig,ej=subplots(1,2,figsize=(15,5))
ej[0].plot(x,exp(-alpha*x**2),lw=2,label=r'$e^{-t^2}$')
ej[0].grid()
ej[0].legend(loc='best')
ej[0].set_xlabel(r'$t$',fontsize=15)
ej[0].set_ylabel(r'$f(t)$',fontsize=15)
ej[1].plot(k,sqrt(pi)*exp(-k**2/(4.*alpha)),lw=2,label=r'$\sqrt{\pi}e^{-\omega^2/4}$')
ej[1].grid()
ej[1].legend(loc='best',fontsize=13)
ej[1].set_xlabel(r'$\omega$',fontsize=15)
ej[1].set_ylabel(r'$\tilde{f}(\omega)$',fontsize=15)
fig.savefig("../figs/fig-Fourier-Gaussiana.pdf")

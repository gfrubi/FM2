# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
style.use('classic')
x=linspace(-10,10,1000)
k=linspace(-10,10,1000)
alpha=1
figure(figsize=(15,5))
subplot(1,2,1)
plot(x,exp(-alpha*x**2),lw=2,label=r'$e^{-t^2}$')
grid()
legend(loc='best', fontsize=15)
xlabel(r'$t$',fontsize=15)
ylabel(r'$f(t)$',fontsize=15)
subplot(1,2,2)
plot(k,sqrt(pi)*exp(-k**2/(4.*alpha)),lw=2,label=r'$\sqrt{\pi}e^{-\omega^2/4}$')
grid()
legend(loc='best',fontsize=15)
xlabel(r'$\omega$',fontsize=15)
ylabel(r'$\tilde{f}(\omega)$',fontsize=15)
savefig("../figs/fig-Fourier-Gaussiana.pdf")

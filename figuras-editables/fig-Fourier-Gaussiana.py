# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')
x = np.linspace(-10,10,1000)
k = np.linspace(-10,10,1000)
alpha = 1
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.plot(x,np.exp(-alpha*x**2),lw=2,label='$e^{-t^2}$')
plt.grid(True)
plt.legend(loc='best', fontsize=15)
plt.xlabel('$t$',fontsize=15)
plt.ylabel('$f(t)$',fontsize=15)
plt.subplot(1,2,2)
plt.plot(k,np.sqrt(np.pi)*np.exp(-k**2/(4.*alpha)),lw=2,label='$\sqrt{\pi}e^{-\omega^2/4}$')
plt.grid(True)
plt.legend(loc='best',fontsize=15)
plt.xlabel('$\omega$',fontsize=15)
plt.ylabel('$\tilde{f}(\omega)$',fontsize=15)
plt.savefig("../figs/fig-Fourier-Gaussiana.pdf")

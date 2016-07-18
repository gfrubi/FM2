# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.special import *

x = linspace(-4,4,1000)
fig = figure(figsize=(8,6),dpi=500)
plot(x,gamma(x),label=r'$\Gamma(x)$', linewidth=2)
#title(ur'Función Gamma de argumento real',fontsize=12)
xlabel('$x$',fontsize=15)
ylabel(r'$\Gamma(x)$',fontsize=15)
grid()
ylim(-6,6)
savefig('../figs/fig-funcion-Gamma.pdf')

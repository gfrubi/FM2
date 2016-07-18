# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.special import laguerre

colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

x = linspace(-5,20,1000)
fig = figure(figsize=(8,6))
for n in range(5):
	plot(x,polyval(laguerre(n),x),colores[n], dashes=dasheses[n],label=r'$L_{%d}(x)$'%n, linewidth=2)
ylim(-10,20)
xlabel('$x$',fontsize=15)
ylabel(r'$L_n(x)$',fontsize=15)
legend(loc='best',fontsize=13)
grid()
savefig('../figs/fig-Laguerre.pdf')

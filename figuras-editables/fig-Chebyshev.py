# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.special import chebyc

colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

x = linspace(-1,1,1000)
fig = figure(figsize=(8,6))
for n in range(5):
	plot(x,polyval(chebyc(n),x),colores[n], dashes=dasheses[n],label=r'$T_{%d}(x)$'%n, linewidth=2)
#ylim(-50,50)
xlabel('$x$',fontsize=15)
ylabel(r'$T_n(x)$',fontsize=15)
legend(loc='best',fontsize=13)
grid()
savefig('../figs/fig-Chebyshev.pdf')

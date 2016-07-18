# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *

def escalon(x,c):
    return 1*(x>=c)


c=0
x=linspace(c-2,c+2,1000)
f=figure(figsize=(8,6))
plot(x,escalon(x,c),lw=2,label=r'$H(t-a)$')
#title(ur'Función escalón $H(t-a)$',fontsize=18)
xticks([0],['$c$'],fontsize=18)
yticks([0,1],['0','1'])
#xlim(-3.5,3.5)
ylim(-0.1,1.1)
grid()
legend(loc='best',fontsize=13)
xlabel('$t$',fontsize=15)
ylabel('$H(t-c)$',fontsize=15)
f.savefig("../figs/fig-funcion-escalon.pdf")

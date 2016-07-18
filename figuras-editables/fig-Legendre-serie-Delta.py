# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *
from math import factorial


def sn_delta(m,x):
    """
    Implementación escalar de la serie truncada hasta orden $n$ de la serie de Fourier de la función delta de dirac con período $T$.
    """    
    sn_delta=0.
    for k in range(m+1):
        sn_delta=sn_delta+((4.*k+1.)/2.)*(((-1)**(k)*factorial(2.*k))/(2.**(2.*k)*factorial(k)**2.))*legendre(2*k)(x)
    return sn_delta
sn_delta_vec=np.vectorize(sn_delta)#vectorizando la función sn_delta

x=np.linspace(-1,1,1000)
fig = plt.figure(figsize=(8,6))
m=50
plt.plot(x,sn_delta_vec(m,x), linewidth=2)
#plt.title('Serie de Legendre de la Delta de Dirac truncada a orden $n=%d$'%m)
plt.grid()
plt.ylim(-10,40)
plt.xlabel('$x$',fontsize=15)
plt.ylabel("$S_{%d}(x)$" % m,fontsize=15)
plt.savefig('../figs/fig-Legendre-serie-Delta.pdf')

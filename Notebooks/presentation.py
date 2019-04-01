import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import quad

def f(t, time_table, x_table, y_table):
    return np.interp(t, time_table, x_table) + 1j*np.interp(t, time_table, y_table)

def Sn(t, coef_list,order=5):
    tau = max(t)-min(t)
    series = np.zeros(len(t),dtype=complex)
    for id,n in enumerate(range(-order, order+1)):
        series += coef_list[id]*np.exp((2*np.pi/tau)*n*1j*t)
    return np.real(series), np.imag(series)

def coef_list(time_table, x_table, y_table, order=5):
    coef_list = []
    tau = max(time_table)-min(time_table)
    for n in range(-order, order+1):
        real_coef = quad(lambda t: np.real(f(t, time_table, x_table, y_table) * np.exp(-(2*np.pi/tau)*n*1j*t)), 0, tau, limit=100, full_output=1)[0]/tau
        imag_coef = quad(lambda t: np.imag(f(t, time_table, x_table, y_table) * np.exp(-(2*np.pi/tau)*n*1j*t)), 0, tau, limit=100, full_output=1)[0]/tau
        coef_list.append(real_coef+1j*imag_coef)
    return np.array(coef_list)

def visualize(x_DFT, y_DFT, tau, coef, order, space, fig_lim):
    fig, ax = plt.subplots()
    lim = max(np.abs(fig_lim))
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_aspect('equal')

    # Initialize
    line = plt.plot([], [], 'k-', linewidth=2)[0]
    radius = [plt.plot([], [], 'r-', linewidth=0.5, marker='o', markersize=1)[0] for _ in range(2 * order + 1)]
    circles = [plt.plot([], [], 'r-', linewidth=0.8)[0] for _ in range(2 * order + 1)]

    def update_c(c, t):
        new_c = []
        for i, n in enumerate(range(-order, order + 1)):
            dtheta = -n*t*(2*np.pi/tau)
            ct, st = np.cos(dtheta), np.sin(dtheta)
            v = (ct*c[i].real + st*c[i].imag)+(-st*c[i].real + ct*c[i].imag)*1j
            new_c.append(v)
        return np.array(new_c)

    def sort_velocity(order):
        idx = []
        for i in range(1,order+1):
            idx.extend([order+i, order-i]) 
        return idx    
    
    def animate(i):
        # animate lines
        line.set_data(x_DFT[:i], y_DFT[:i])
        # animate circles
        r = np.abs(coef)
        pos = coef[order]
        c = update_c(coef, i*(tau/len(space)))
        idx = sort_velocity(order)
        for j, rad, circle in zip(idx,radius,circles):
            new_pos = pos + c[j]
            rad.set_data([pos.real, new_pos.real], [pos.imag, new_pos.imag])
            theta = np.linspace(0, 2*np.pi, 50)
            x, y = r[j]*np.cos(theta) + pos.real, r[j]*np.sin(theta) + pos.imag
            circle.set_data(x, y)
            pos = new_pos
                
    # Animation
    ani = animation.FuncAnimation(fig, animate, frames=len(space), interval=5)
    return ani

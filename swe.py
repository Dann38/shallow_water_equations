import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
# %matplotlib notebook


N = 100
M = 2000
L = 50
T = 6

H = np.zeros((N, M))
V = np.zeros((N, M))

x = np.linspace(0, L, N)

H[:,0]= 5+ 2*np.exp(-(0.2*(x-L/2))**2) + np.sin(x*np.pi/5)*0.2 
V[:,0] = 0.3


rez = []

dt = T/M
dx = L/N

g = 9.81

for j in range(M-1):
    
    dh = np.zeros(N)
    dv = np.zeros(N)
    dh[1:-1] =  (H[2:, j]-H[:-2, j])/(2*dx)
    dh[-1] = (H[-1, j] - H[-2, j])/(dx)
    dh[0] = (H[1, j] - H[0, j])/(dx)
    dv[1:-1] =  (V[2:, j]-V[:-2, j])/(2*dx)
    dv[-1] = (V[-1, j] - V[-2, j])/(dx)
    dv[0] = (V[1, j] - V[0, j])/(dx)

    H[:, j+1] = H[:, j]-dt*dh*V[:, j] -dt*dv*H[:, j]
    V[:, j+1] = V[:, j]-dt*dh*g -dt*dv*V[:, j]

    # Отражение
    V[-1, j+1] = - V[-2, j+1] 
    V[0, j+1] = - V[1, j+1] 

fig, ax = plt.subplots()

ax.set(xlim=[0, 50], ylim=[0, 10])
ax.legend()
line = ax.plot(x, H[:, 0], label=f'v0 = {0} m/s')[0]

def update(frame):
    y = H[:, frame]
    line.set_ydata(y)
    return line,


ani = FuncAnimation(fig=fig, func=update, frames=M, interval=30)
ani.save("name2.gif")


import phyEng as pe
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from scipy.interpolate import interp2d

fig, ax = plt.subplots()
ax.set_xlim(0, 10)

scat = ax.scatter(1, 0)
print(scat)
x = np.linspace(0, 10)
print(x)


def animate(i):
    scat.set_offsets((x[i], 0))
    return scat


anim = anim.FuncAnimation(fig, animate, repeat=True,
                          frames=len(x)-1, interval=50)

plt.show()

ball = pe.object(mass=20)
earth = pe.object(mass=6E24, radius=6.371E6)






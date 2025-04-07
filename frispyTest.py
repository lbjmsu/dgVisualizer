import frispy.disc
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import random

# phi is nose angle
# theta is amt hyzer (negative theta is hyzer while positive theta is anhyzer)
# initial gamma is rotation of disc around axis perpendicular to flight plate, but change in gamma is spin speed
#   positive dgamma is RHFH
#   negative dgamma is RHBH

# ----- Next goal is to better determine which parameter is analogous to what term in disc golf

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
dgammas = np.arange(0,150,15)
color = np.linspace(0, 1, num=dgammas.size)

for i, dgamma in enumerate(dgammas):
    disc = frispy.disc.Disc(z=1,vy=30,vx=0,vz=0.1,theta=0,phi=0,dgamma=-dgamma,dtheta=-0.5)

    result = disc.compute_trajectory()[0]
    times = result['times']
    x = result['x']
    y = result['y'] # Apparently Y is NOT height
    z = result['z']

    c = (color[i], color[i], 0.35, 0.3)

    sc = ax.scatter(x,y,z,color=c,label=f'Spin Speed (rpm): {np.floor(dgamma /(2*np.pi) * 60)}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z (Height)')

fig.legend()

plt.show()

print("Hello")

import frispy.disc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# create 3d plt subplot
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set(xlim=(0,30), ylim=(-15,15), zlim=(-5,5), xlabel="X", ylabel="Y", zlabel="Z")
ax.view_init(elev=12, azim=180)

# create disc objects
hyzer_angles = -np.array([-25, -20, -15, -10, -5]) # sign of angle = sign of rpm  =  anhyzer
thetas = hyzer_angles * np.pi / 180

rpm = 600
dgamma = rpm / 60 * np.pi * 2

dtheta = 0 # stability?

vx = 8
z = 5

d0 = frispy.disc.Disc(z=z, theta = thetas[0], phi = -thetas[0]/5, vz = hyzer_angles[0]/5, vx = vx, dtheta=dtheta, dgamma = dgamma)
d1 = frispy.disc.Disc(z=z, theta = thetas[1], phi = -thetas[1]/5, vz = hyzer_angles[1]/5, vx = vx, dtheta=dtheta, dgamma = dgamma)
d2 = frispy.disc.Disc(z=z, theta = thetas[2], phi = -thetas[2]/5, vz = hyzer_angles[2]/5, vx = vx, dtheta=dtheta, dgamma = dgamma)
d3 = frispy.disc.Disc(z=z, theta = thetas[3], phi = -thetas[3]/5, vz = hyzer_angles[3]/5, vx = vx, dtheta=dtheta, dgamma = dgamma)
d4 = frispy.disc.Disc(z=z, theta = thetas[4], phi = -thetas[4]/5, vz = hyzer_angles[4]/5, vx = vx, dtheta=dtheta, dgamma = dgamma)

# determine their flight path

d0_results = d0.compute_trajectory(flight_time=6)
d1_results = d1.compute_trajectory(flight_time=6)
d2_results = d2.compute_trajectory(flight_time=6)
d3_results = d3.compute_trajectory(flight_time=6)
d4_results = d4.compute_trajectory(flight_time=6)

# store these flight paths

x0, y0, z0 = d0_results[0]['x'], d0_results[0]['y'], d0_results[0]['z']
x1, y1, z1 = d1_results[0]['x'], d1_results[0]['y'], d1_results[0]['z']
x2, y2, z2 = d2_results[0]['x'], d2_results[0]['y'], d2_results[0]['z']
x3, y3, z3 = d3_results[0]['x'], d3_results[0]['y'], d3_results[0]['z']
x4, y4, z4 = d4_results[0]['x'], d4_results[0]['y'], d4_results[0]['z']

# use these flight paths as input to artist objects

line0, = ax.plot(x0[0], y0[0], z0[0], color=(0, 0, 1), label=f"{-hyzer_angles[0]} degrees anhyzer")
line1, = ax.plot(x1[0], y1[0], z1[0], color=(0, 0, 0.8), label=f"{-hyzer_angles[1]} degrees anhyzer")
line2, = ax.plot(x2[0], y2[0], z2[0], color=(0, 0, 0.6), label=f"{-hyzer_angles[2]} degrees anhyzer")
line3, = ax.plot(x3[0], y3[0], z3[0], color=(0, 0, 0.4), label=f"{-hyzer_angles[3]} degrees anhyzer")
line4, = ax.plot(x4[0], y4[0], z4[0], color=(0, 0, 0.2), label=f"{-hyzer_angles[4]} degrees anhyzer")

# create function to update these artist objects

def update(frame):
    x_sub0, y_sub0, z_sub0 = x0[:frame], y0[:frame], z0[:frame]
    x_sub1, y_sub1, z_sub1 = x1[:frame], y1[:frame], z1[:frame]
    x_sub2, y_sub2, z_sub2 = x2[:frame], y2[:frame], z2[:frame]
    x_sub3, y_sub3, z_sub3 = x3[:frame], y3[:frame], z3[:frame]
    x_sub4, y_sub4, z_sub4 = x4[:frame], y4[:frame], z4[:frame]

    data0 = np.stack([x_sub0, y_sub0, z_sub0])
    data1 = np.stack([x_sub1, y_sub1, z_sub1])
    data2 = np.stack([x_sub2, y_sub2, z_sub2])
    data3 = np.stack([x_sub3, y_sub3, z_sub3])
    data4 = np.stack([x_sub4, y_sub4, z_sub4])

    line0.set_data(data0[:2])
    line1.set_data(data1[:2])
    line2.set_data(data2[:2])
    line3.set_data(data3[:2])
    line4.set_data(data4[:2])

    line0.set_3d_properties(data0[2])
    line1.set_3d_properties(data1[2])
    line2.set_3d_properties(data2[2])
    line3.set_3d_properties(data3[2])
    line4.set_3d_properties(data4[2])

    return (line0, line1, line2, line3, line4)

# create animation

frames = len(x0)

ani = animation.FuncAnimation(fig, func=update, frames=frames, interval=50)
plt.legend(loc="lower left")
# ani.save("RHBH_Anhyzer_Test.gif")

# ax.view_init(elev=76, azim=180)
# ani.save("RHBH_Anhyzer_Test_2.gif")

plt.show()

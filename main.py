import numpy as np
import matplotlib.pyplot as plt

from physics import pendulum_derivative
from solvers import euler_solver, euler_cromer_solver

#%% Set constants.
g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 5       # mass              [kg]

consts = (g, L, m)

start = 0
stop = 9
dt = 0.1

initial_state = (0.2, 0)                      # initial theta [rad] and omega [rad/s]
times = np.arange(start, stop + dt, dt)       # times at which to evaluate position [s]

#%% Solve using Euler's method.
euler_states = euler_solver(pendulum_derivative, initial_state, times, consts)
euler_theta = euler_states[:,0]
euler_omega = euler_states[:,1]
euler_energy = m*g*L*(1 - np.cos(euler_theta)) + 0.5*m* L**2 * euler_omega**2

#%% Solve using the Euler-Cromer method.
euler_cromer_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts)
euler_cromer_theta = euler_cromer_states[:,0]
euler_cromer_omega = euler_cromer_states[:,1]
euler_cromer_energy = m*g*L*(1 - np.cos(euler_cromer_theta)) + 0.5*m* L**2 * euler_cromer_omega**2

#%% Compare both methods visually.
plt.plot(times, euler_theta, label="Euler's Method")
plt.plot(times, euler_cromer_theta, label="Euler-Cromer Method")
plt.title("Pendulum Angle vs. Time: Euler and Euler-Cromer")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.legend()
plt.savefig("euler_vs_euler-cromer_angle.png")

plt.figure()
plt.plot(times[:20], euler_energy[:20], label="Euler's Method")
plt.plot(times[:20], euler_cromer_energy[:20], label="Euler-Cromer Method")
plt.title("Pendulum Energy vs. Time: Euler and Euler-Cromer")
plt.xlabel("Time [s]")
plt.ylabel("Energy [J]")
plt.legend()
plt.savefig("euler_vs_euler-cromer_energy.png")
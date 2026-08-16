import numpy as np
import matplotlib.pyplot as plt

from physics import linear_derivative, pendulum_derivative, pendulum_drag_derivative
from solvers import euler_solver, euler_cromer_solver
from animation import animate_pendulum

#---------------------------------------

#%% Set constants.
g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 5       # mass              [kg]

consts = (g, L, m)

initial_state = (0.1, 0)            # initial theta [rad] and omega [rad/s]
times = np.arange(0, 4, 0.1)        # times at which to evaluate position [s]

#%% Solve using Euler's method.
euler_states = euler_solver(linear_derivative, initial_state, times, consts)
euler_theta = euler_states[:,0]
euler_omega = euler_states[:,1]
euler_energy = 0.5*m*g*L* euler_theta**2 + 0.5*m* L**2 * euler_omega**2

#%% Solve using the Euler-Cromer method.
euler_cromer_states = euler_cromer_solver(linear_derivative, initial_state, times, consts)
euler_cromer_theta = euler_cromer_states[:,0]
euler_cromer_omega = euler_cromer_states[:,1]
euler_cromer_energy = 0.5*m*g*L* euler_cromer_theta**2 + 0.5*m* L**2 * euler_cromer_omega**2

#%% Compare the angle and relative energy error of the two methods.
plt.figure(figsize=(10, 5))
plt.suptitle("Euler vs. Euler-Cromer: Linearized Pendulum", fontsize=13)

# Subplot 1: Pendulum angle
plt.subplot(1, 2, 1)
plt.plot(times, euler_theta, label="Euler's Method")
plt.plot(times, euler_cromer_theta, label="Euler-Cromer Method")
plt.title("Angle vs. Time")
plt.xlabel(r"Time, $t$ (s)")
plt.ylabel(r"Angle, $\theta$ (rad)")
plt.legend()

# Subplot 2: Relative energy error
euler_energy_error = (euler_energy - euler_energy[0]) / euler_energy[0]
euler_cromer_energy_error = (euler_cromer_energy - euler_cromer_energy[0]) / euler_cromer_energy[0]

plt.subplot(1, 2, 2)
plt.plot(times, euler_energy_error, label="Euler's Method")
plt.plot(times, euler_cromer_energy_error, label="Euler-Cromer Method")
plt.title("Relative Energy Error vs. Time")
plt.xlabel(r"Time, $t$ (s)")
plt.ylabel(r"Relative Energy Error, $\Delta E / E_0$ (%)")
plt.legend()

plt.tight_layout()
plt.savefig("euler_vs_euler-cromer.png")

#---------------------------------------

#%% Phase Space plot of Euler vs. Euler-Cromer
plt.figure()
plt.plot(euler_theta, euler_omega, label="Euler's Method")
plt.plot(euler_cromer_theta, euler_cromer_omega, label="Euler-Cromer Method")
plt.title("Euler vs. Euler-Cromer: Linearized Pendulum Phase Space")
plt.xlabel(r"Angle, $\theta$ (rad)")
plt.ylabel(r"Angular Velocity, $\omega$ (rad/s)")
plt.legend()
plt.savefig("euler_vs_euler-cromer_phase_space.png")
plt.axis("equal")

#---------------------------------------

#%% Phase Space of the Nonlinear Pendulum
plt.figure()
times = np.arange(0, 7 + 0.1, 0.03)       # times at which to evaluate position [s]

g = 9.8     # gravity                 [m/s^2]
L = 1       # pendulum length         [m]
m = 5       # mass                    [kg]

consts = (g, L, m)

initial_state = (0.5,0)      # Initial angle [rad] and initial angular velocity [rad/s]
undamped_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts)
plt.plot(undamped_states[:,0], undamped_states[:,1], label='Low-Amplitude Oscillation')

initial_state = (1.3,0)      # Initial angle [rad] and initial angular velocity [rad/s]
undamped_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts)
plt.plot(undamped_states[:,0], undamped_states[:,1], label='Medium-Amplitude Oscillation')

initial_state = (2.9,0)      # Initial angle [rad] and initial angular velocity [rad/s]
undamped_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts)
plt.plot(undamped_states[:,0], undamped_states[:,1], label='High-Amplitude Oscillation')

initial_state = (0,7)      # Initial angle [rad] and initial angular velocity [rad/s]
undamped_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts)
plt.plot(undamped_states[:,0], undamped_states[:,1], label='Rotation')

# Plot the Separatrix
all_thetas = np.arange(0, 35, 0.1)
plt.plot(all_thetas, 2*np.sqrt(g/L) * np.cos(all_thetas/2), "--", color='black', label='Separatrix', linewidth=0.7)
plt.plot(all_thetas, -2*np.sqrt(g/L) * np.cos(all_thetas/2), "--", color='black', linewidth=0.7)

# Stable Equilibria
plt.plot([0,2*np.pi,4*np.pi,6*np.pi,8*np.pi,10*np.pi],[0,0,0,0,0,0],'ko', ms=1)

plt.xlabel(r"Angle, $\theta$ (rad)")
plt.ylabel(r"Angular Velocity, $\omega$ (rad/s)")
plt.title("Phase Space Dynamics of the Nonlinear Pendulum")
plt.legend()
plt.ylim(-10, 20)
plt.gca().set_aspect("equal", adjustable="box")
plt.savefig("pendulum_phase_space.png")

#---------------------------------------

#%% Animation of Damped Pendulum Motion, Phase Space, and Energy
dt = 0.05
times = np.arange(0, 10, dt)

g = 9.8
L = 1
m = 5
b = 0.3

consts = (g, L, m, b)
initial_state = (0, 9)

states = euler_cromer_solver(pendulum_drag_derivative, initial_state, times, consts)
movie = animate_pendulum(states, times, consts)
plt.rcParams['animation.embed_limit'] = 50
movie.save("damped_phase_space.mp4", writer="ffmpeg", fps=1/dt)

###################################################
# Commensurability and Stroboscopic Phase Drift

g = 9.8
L = 1
m = 5

period = 2*np.pi*np.sqrt(L/g)
consts = (g, L, m)

initial_state = (0.5, 0)

# Create 2x2 figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ============================================================
# Case 1: T_sample = T0/3
# ============================================================

strobe_period = period / 3
times = np.arange(0, 50, strobe_period/100)

states = euler_cromer_solver(
    linear_derivative,
    initial_state,
    times,
    consts
)

theta = states[:, 0]
omega = states[:, 1]

# Top-left: Phase space
ax1 = axes[0, 0]
ax1.plot(theta, omega)
ax1.plot(theta[::100], omega[::100], 'o-', linewidth=0.5)

ax1.set_title(r"Phase Space — $T_{\mathrm{sample}}=T_0/3$")
ax1.set_xlabel(r"Angle, $\theta$ [rad]")
ax1.set_ylabel(r"Angular Velocity, $\omega$ [rad/s]")

# Top-right: Angle vs time
ax2 = axes[0, 1]

y_lim = 0.55 * np.ptp(theta[:3000])

ax2.plot(times[:3000], theta[:3000], color='orange')
ax2.vlines(
    times[:3000:100],
    -y_lim,
    y_lim,
    alpha=0.5,
    label='Stroboscopic Sampling Times'
)

ax2.set_title(r"Angle vs. Time — $T_{\mathrm{sample}}=T_0/3$")
ax2.set_xlabel(r"Time, $t$ [s]")
ax2.set_ylabel(r"Angle, $\theta$ [rad]")
ax2.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))

# ============================================================
# Case 2: T_sample = T0/3.05
# ============================================================

strobe_period = period / 3.05
times = np.arange(0, 50, strobe_period/100)

states = euler_cromer_solver(
    linear_derivative,
    initial_state,
    times,
    consts
)

theta = states[:, 0]
omega = states[:, 1]

# Bottom-left: Phase space
ax3 = axes[1, 0]
ax3.plot(theta, omega)
ax3.plot(theta[::100], omega[::100], 'o-', linewidth=0.5)

ax3.set_title(r"Phase Space — $T_{\mathrm{sample}}=T_0/3.05$")
ax3.set_xlabel(r"Angle, $\theta$ [rad]")
ax3.set_ylabel(r"Angular Velocity, $\omega$ [rad/s]")

# Bottom-right: Angle vs time
ax4 = axes[1, 1]

y_lim = 0.55 * np.ptp(theta[:3000])

ax4.plot(times[:3000], theta[:3000], color='orange')
ax4.vlines(
    times[:3000:100],
    -y_lim,
    y_lim,
    alpha=0.5,
    label='Stroboscopic Sampling Times'
)

ax4.set_title(r"Angle vs. Time — $T_{\mathrm{sample}}=T_0/3.05$")
ax4.set_xlabel(r"Time, $t$ [s]")
ax4.set_ylabel(r"Angle, $\theta$ [rad]")
ax4.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))

# ============================================================
# Overall formatting
# ============================================================

fig.suptitle("Commensurability and Stroboscopic Phase Drift", fontsize=16)

plt.tight_layout()
plt.savefig("stroboscope_basics.png")


#######################################################
# Amplitude-Dependent Period and Stroboscopic Alignment

g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 1       # mass              [kg]
b = 0.07

period = 2*np.pi*np.sqrt(L/g)
strobe_period = period / 3
consts = (g, L, m, b)

initial_state = (0.5, 0)                                  # initial theta [rad] and omega [rad/s]
times = np.arange(0, 50, strobe_period/100)               # times at which to evaluate position [s]

states = euler_cromer_solver(pendulum_drag_derivative, initial_state, times, consts)
theta = states[:,0]
omega = states[:,1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle(r"Amplitude-Dependent Period and Stroboscopic Alignment — $T_{\mathrm{sample}}=T_0/3$", fontsize=13)

# Left: phase-space plot
ax1.plot(theta, omega)
ax1.plot(theta[::100], omega[::100], 'o-', linewidth=0.5)
ax1.set_title("Phase Space with Stroboscopic Samples")
ax1.set_xlabel(r"Angle, $\theta$ [rad]")
ax1.set_ylabel(r"Angular Velocity, $\omega$ [rad/s]")

# Right: angle vs time
y_lim = 0.55 * np.ptp(theta[:3000])
ax2.plot(times[:3000], theta[:3000], color='orange')
ax2.vlines(times[:3000:100], -y_lim, y_lim, alpha=0.5, label='Stroboscopic Sampling Times')
ax2.set_title("Angle vs. Time")
ax2.set_xlabel(r"Time, $t$ [s]")
ax2.set_ylabel(r"Angle, $\theta$ [rad]")
ax2.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98), borderaxespad=0)

plt.tight_layout()
plt.savefig("stroboscope_pendulum.png")

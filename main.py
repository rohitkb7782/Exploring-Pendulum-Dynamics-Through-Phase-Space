import numpy as np
import matplotlib.pyplot as plt

from physics import pendulum_derivative, pendulum_drag_derivative, pendulum_driven_derivative
from solvers import euler_solver, euler_cromer_solver
from analysis import get_peaks, get_periods

#### --------- SECTION I: Undamped Pendulum --------- ####
#%% Set constants.
g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 5       # mass              [kg]

consts = (g, L, m)

start = 0
stop = 8
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
plt.title("Pendulum Angle vs. Time: Euler vs. Euler-Cromer")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.legend()
plt.savefig("euler_vs_euler-cromer_angle.png")

plt.figure()
euler_energy_error = (euler_energy - euler_energy[0]) / euler_energy[0]
euler_cromer_energy_error = (euler_cromer_energy - euler_cromer_energy[0]) / euler_cromer_energy[0]
plt.plot(times[:30], euler_energy_error[:30], label="Euler's Method")
plt.plot(times[:30], euler_cromer_energy_error[:30], label="Euler-Cromer Method")
plt.title("Relative Energy Error: Euler vs. Euler-Cromer")
plt.xlabel("Time [s]")
plt.ylabel("Relative Energy Error [%]")
plt.legend()
plt.savefig("euler_vs_euler-cromer_energy_error.png")

# Initialize constants.
plt.figure()
start = 0
stop = 30
dt = 0.01

normal_resolution = 100
spike_resolution = 100

# Create a list of initial angles with finer resolution at where the graph will peak.
early_angles = np.linspace(0.05, 3.14, normal_resolution)
spike_angles = np.linspace(3.1, 3.2, spike_resolution)
last_angles = np.linspace(3.15, 2*np.pi, normal_resolution)
all_angles = np.concatenate((early_angles, spike_angles, last_angles))

initial_states_list = np.zeros( (len(all_angles), 2) )
for i in range(len(all_angles)):
    initial_states_list[i,0] = all_angles[i]

# Find the period for each initial angle.
times = np.arange(start, stop + dt, dt)
periods = np.zeros_like(all_angles)
for i in range(len(all_angles)):
    states = euler_cromer_solver(pendulum_derivative, initial_states_list[i,:], times, consts)
    theta = states[:,0]
    periods[i] = np.mean(get_periods(times, theta))

plt.plot(all_angles, periods)
plt.title("Pendulum Period vs. Initial Angle")
plt.xlabel("Initial Angle [rad]")
plt.ylabel("Period [s]")
plt.savefig("period_vs_angle.png")

#### --------- SECTION II: Damped Pendulum --------- ####
#%% Set constants.
plt.figure()
g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 5       # mass              [kg]
b = 0.4     # linear air resistance   [kg/s]

consts = (g, L, m, b)

start = 0
stop = 16
dt = 0.1

initial_state = (0, 7.2)                      # initial theta [rad] and omega [rad/s]
times = np.arange(start, stop + dt, dt)       # times at which to evaluate position [s]

#%% Solve and graph the angle as a function of time.
states = euler_cromer_solver(pendulum_drag_derivative, initial_state, times, consts)
theta = states[:,0]
plt.plot(times, theta)
plt.title("Damped Pendulum Motion at a Large Amplitude")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.ylim(top=theta.max() + 0.5)

# Choose a few consecutive peaks and add the period annotations.
peak_indexes, _ = get_peaks(theta)
for i in [0, 1, 2, 3]:
    t1 = times[peak_indexes[i]]
    t2 = times[peak_indexes[i + 1]]
    y = theta[peak_indexes[i]] + 0.1

    plt.annotate(
        "",
        xy=(t2, y),
        xytext=(t1, y),
        arrowprops=dict(arrowstyle="<->")
    )

    plt.text(
        (t1 + t2) / 2,
        y + 0.05,
        f"T = {t2 - t1:.2f} s",
        ha="center"
    )
plt.savefig("damped_angle.png")

#%% Phase Space: Damped and Undamped
plt.figure()
times = np.arange(0, 7 + 0.1, 0.1)       # times at which to evaluate position [s]

g = 9.8     # gravity                 [m/s^2]
L = 1       # pendulum length         [m]
m = 5       # mass                    [kg]
b = 0.3     # linear air resistance   [kg/s]

consts = (g, L, m, b)

# Plot two sets of initial conditions that evolve undamped and then damped
initial_state = (1,0)      # Initial angle [rad] and initial angular velocity [rad/s]
undamped_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts[:3])
plt.plot(undamped_states[:,0], undamped_states[:,1], label='Undamped Oscillation')
damped_states = euler_cromer_solver(pendulum_drag_derivative, initial_state, times, consts)
plt.plot(damped_states[:,0], damped_states[:,1], label='Damped Oscillation')

initial_state = (0,7)
undamped_states = euler_cromer_solver(pendulum_derivative, initial_state, times, consts[:3])
plt.plot(undamped_states[:,0], undamped_states[:,1], label='Undamped rotation')
damped_states = euler_cromer_solver(pendulum_drag_derivative, initial_state, times, consts)
plt.plot(damped_states[:,0], damped_states[:,1], label='Damped Rotation → Oscillation')

# Plot the Separatrix
all_thetas = np.arange(0, 35, 0.1)
plt.plot(all_thetas, 2*np.sqrt(g/L) * np.cos(all_thetas/2), "--", color='black', label='Separatrix')

plt.xlabel("Angle [rad]")
plt.ylabel("Angular Velocity [rad/s]")
plt.title("Phase-Space Dynamics of the Damped and Undamped Pendulum")
plt.ylim(top=15)
plt.legend()
plt.savefig("phase_space.png")

#### --------- SECTION III: Driven Pendulum --------- ####
plt.figure()
g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 5       # mass              [kg]
b = 0.1     # linear air resistance   [kg/s]
Tau_0 = 2     
omega_0 = 0.3

consts = (g, L, m, b, Tau_0, omega_0)

initial_state = (0.3, 0)                  # initial theta [rad] and omega [rad/s]
times = np.arange(0, 80 + 0.1, 0.1)       # times at which to evaluate position [s]

states = euler_cromer_solver(pendulum_driven_derivative, initial_state, times, consts)
theta = states[:,0]
omega = states[:,1]
plt.plot(times, theta)

plt.title("Transient and Steady-State Response of a Driven Pendulum")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.savefig("driven_pendulum.png")

#%% Resonance Curves
plt.figure()
g = 9.8     # gravity           [m/s^2]
L = 1       # pendulum length   [m]
m = 5       # mass              [kg]
b_list = [1.5, 0.35, 0.7]
Tau_0 = 1

initial_state = (0.5, 0)                  # initial theta [rad] and omega [rad/s]
times = np.arange(0, 80 + 0.1, 0.1)       # times at which to evaluate position [s]

frequencies = np.linspace(0, 6, 361)

for b in b_list:
    amplitudes = []
    for omega_0 in frequencies:
        # Get amplitude of steady-state motion (average of all peaks of later half of motion)
        consts = (g, L, m, b, Tau_0, omega_0)
        states = euler_cromer_solver(pendulum_driven_derivative, initial_state, times, consts)
        late_thetas = states[400:,0]
        _, peak_thetas = get_peaks(late_thetas)
        amplitudes.append(np.mean(peak_thetas))
    
    plt.plot(frequencies, amplitudes, label='b='+str(b))

plt.title("Resonance Curves for Different Damping Coefficients")
plt.xlabel("Driving Frequency, [rad/s]")
plt.ylabel("Steady-State Amplitude [rad]")
plt.legend()
plt.savefig("resonance.png")
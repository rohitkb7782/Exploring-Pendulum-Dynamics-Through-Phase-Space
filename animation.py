import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_pendulum(states, times, consts):
    g, L, m, b = consts
    theta = states[:, 0]
    omega = states[:, 1]
    
    # Physical pendulum position
    visual_L = 5
    x = visual_L * np.sin(theta)
    y = -visual_L * np.cos(theta)

    # Energy
    KE = 0.5 * m * L**2 * omega**2
    PE = m * g * L * (1 - np.cos(theta))
    E = KE + PE

    # Two plots on top, one wide plot on bottom
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle("Damped Pendulum: From Rotation to Oscillation", y=0.98, fontsize=13)
    gs = fig.add_gridspec(2, 2, height_ratios=[3, 1], top=0.90)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, :])

    # Animation Time Displayer
    time_text = fig.text(0.5, 0.925, "", ha="center", fontsize=12)
    
    # =========================================================
    # LEFT: Pendulum
    # =========================================================
    
    bound = 1.2 * visual_L
    ax1.set_xlim(-bound, bound)
    ax1.set_ylim(-bound, bound)
    ax1.set_aspect('equal', adjustable='box')
    ax1.set_title("Pendulum Motion")
    ax1.set_xlabel(r"Horizontal Position, $x$ [m]")
    ax1.set_ylabel(r"Vertical Position, $y$ [m]")
    
    # Pendulum rod and bob
    pendulum_line, = ax1.plot([], [], lw=2)
    pendulum_point, = ax1.plot([], [], 'ro', ms=9)
    ax1.plot([0], [0], 'ko', ms=5)   # pivot

    # Velocity arrow
    velocity_arrow = ax1.quiver(
        0, 0, 0, 0,
        angles='xy', 
        scale_units='xy', 
        scale=10
    )
    arrow_scale = 0.5
    
    # =========================================================
    # RIGHT: Phase space
    # =========================================================
    
    theta_margin = 0.1 * np.ptp(theta)
    omega_margin = 0.1 * np.ptp(omega)
    
    ax2.set_xlim(theta.min() - 2*theta_margin, theta.max() + 2*theta_margin)
    ax2.set_ylim(omega.min() - 2*omega_margin, omega.max() + 2*omega_margin)
    ax2.set_xlabel(r'Angle, $\theta$ [rad]')
    ax2.set_ylabel(r'Angular Velocity, $\omega$ [rad/s]')
    ax2.set_title("Phase Space")
    
    # Separatrix
    all_thetas = np.linspace(ax2.get_xlim()[0], ax2.get_xlim()[1], 1000)
    separatrix = (2 * np.sqrt(g / L) * np.cos(all_thetas / 2))
    ax2.plot(all_thetas, separatrix, "--", color="black", linewidth=0.7, label="Undamped Separatrix")
    ax2.plot(all_thetas, -separatrix, "--", color="black", linewidth=0.7)
    ax2.legend()
    
    # Phase-space trajectory and current point
    phase_line, = ax2.plot([], [])
    phase_point, = ax2.plot([], [], 'o', color='purple', ms=3)

    # State Displayer
    state_text = ax2.text(
        0.03, 0.97, "",
        transform=ax2.transAxes,
        va="top",
        fontsize=10
    )

    # =========================================================
    # BOTTOM: Energy
    # =========================================================
    
    ax3.set_xlim(times[0], times[-1])
    energy_margin = 0.1 * np.ptp(E)
    ax3.set_ylim(min(0, E.min() - energy_margin), E.max() + energy_margin)
    
    ax3.set_title("Energy", fontsize=10)
    ax3.set_xlabel(r"Time, $t$ [s]", fontsize=9)
    ax3.set_ylabel(r"Energy, $E$ [J]", fontsize=9)
    
    ax3.tick_params(labelsize=8)
    
    # Energy Curve
    energy_line, = ax3.plot([], [], label="Total Energy")
    energy_point, = ax3.plot([], [], 'o', color='purple', ms=4)

    # Separatrix Energy
    all_times = np.linspace(ax3.get_xlim()[0], ax3.get_xlim()[1], 1000)
    separatrix_line, = ax3.plot(all_times, 2*m*g*L*np.ones_like(all_times), 'k--', label="Separatrix Energy", linewidth=0.85)
    ax3.legend()
    
    # =========================================================
    # Animation function
    # =========================================================
    
    def get_step(n):
        # Pendulum
        pendulum_line.set_data([0, x[n]], [0, y[n]])
        pendulum_point.set_data([x[n]], [y[n]])

        # Bob velocity
        vx = arrow_scale * visual_L * omega[n] * np.cos(theta[n])
        vy = arrow_scale * visual_L * omega[n] * np.sin(theta[n])
        velocity_arrow.set_offsets([[x[n], y[n]]])
        velocity_arrow.set_UVC(vx, vy)
    
        # Phase space
        phase_line.set_data(theta[:n+1], omega[:n+1])
        phase_point.set_data([theta[n]], [omega[n]])

        # Energy
        energy_line.set_data(times[:n+1], E[:n+1])
        energy_point.set_data([times[n]], [E[n]])

        # State and Time
        state_text.set_text(
            f"$\\theta$ = {theta[n]:.2f} rad\n"
            f"$\\omega$ = {omega[n]:.2f} rad/s"
        )
        
        time_text.set_text(f"t = {times[n]:.2f} s")
    
        return (pendulum_line, pendulum_point, velocity_arrow,
                phase_line, phase_point,
                energy_line, energy_point,
                state_text, time_text)
    
    # =========================================================
    # Create animation
    # =========================================================
    
    my_movie = FuncAnimation(
        fig,
        get_step,
        frames=len(theta),
        interval= (times[1]-times[0]) * 1000,
    )
    
    return my_movie
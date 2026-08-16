# Exploring Pendulum Dynamics Through Phase Space

A computational physics project investigating how phase space can be used to visualize and interpret the dynamics of a pendulum. The project begins with numerical integration and a comparison of Euler's Method and Euler-Cromer, then uses phase-space geometry to examine the transition from linear to nonlinear behavior, the effects of damping, and the structure revealed by stroboscopic sampling.

![Phase space](files/stroboscope_pendulum.png?raw=true)

**Figure 6.** [Opening figure/collage to be selected.]

## Motivation

### Phase Space

Motion is often represented by plotting a variable such as position or angle against time. While this shows how a system evolves, it can hide the underlying structure of that motion. Phase space provides a different perspective by representing the state of a system through its position and velocity. For the pendulum, this state is

$$
(\theta,\omega),
$$

where $\theta$ is the angular displacement and $\omega=\dot{\theta}$ is the angular velocity.

The resulting trajectory gives a geometric view of the dynamics. Periodic oscillations appear as closed curves, rotational motion follows different trajectories, and the boundary between these regimes appears as a separatrix. Numerical error, damping, and nonlinear effects can therefore be studied through changes in phase-space geometry.

Rather than asking only *where is the pendulum at a given time?*, phase space allows us to ask *what states can the pendulum occupy, and how does it move between them?*

### The Pendulum

The pendulum is a simple system that contains several important features of nonlinear dynamics. At small angles, it can be approximated as a linear harmonic oscillator through

$$
\sin\theta \approx \theta,
$$

providing a direct comparison between linear and nonlinear behavior within the same physical system.

At larger amplitudes, nonlinear effects distort the phase-space trajectories and produce a separatrix between oscillatory and rotational motion. Damping adds another layer by causing the system to lose energy and potentially move between these dynamical regimes.

The pendulum therefore provides a compact setting for exploring how numerical methods, nonlinearity, energy, and damping shape the geometry of a dynamical system.

### Research Question

> **How does the geometry of phase space reveal the dynamics of a pendulum?**

This question guides the project from numerical simulation to phase-space analysis, using computation not simply to model the pendulum, but to reveal the structure of its dynamics.

## Mathematical Model

### Pendulum Equation

Consider a pendulum of length $L$ and mass $m$, with angular displacement $\theta$ measured from the downward vertical. In the absence of damping or external forcing, its equation of motion is

$$
\ddot{\theta}+\frac{g}{L}\sin\theta=0,
$$

where $g$ is the acceleration due to gravity.

Writing the equation as a first-order system,

$$
\dot{\theta}=\omega,
\qquad
\dot{\omega}=-\frac{g}{L}\sin\theta.
$$

The state variables used to construct the phase-space trajectories are therefore

$$
(\theta,\omega).
$$

### Linearized Pendulum

For small angular displacements,

$$
\sin\theta\approx\theta,
$$

so the equation becomes

$$
\ddot{\theta}+\frac{g}{L}\theta=0.
$$

This is the equation of a simple harmonic oscillator with natural frequency

$$
\omega_0=\sqrt{\frac{g}{L}}.
$$

The linearized model provides a useful reference for the full nonlinear system. At small amplitudes, their behavior is nearly identical, but at larger amplitudes the approximation breaks down and the phase-space geometry begins to diverge.

### Damped Pendulum

To investigate energy loss, a damping term is added:

$$
\ddot{\theta}+b\dot{\theta}+\frac{g}{L}\sin\theta=0,
$$

where $b$ is the damping coefficient.

Damping causes the mechanical energy of the pendulum to decrease over time. In phase space, this changes the trajectories from closed curves into inward spirals, allowing the system to transition from higher-energy motion toward oscillations around the stable equilibrium.

### Energy and the Separatrix

For the undamped pendulum, the mechanical energy is conserved. The kinetic and potential energies are

$$
K=\frac{1}{2}mL^2\omega^2
$$

and

$$
U=mgL(1-\cos\theta),
$$

giving

$$
E=K+U.
$$

The unstable equilibrium occurs at $\theta=\pi$, where the pendulum is inverted. The energy required to reach this point from the stable equilibrium is

$$
E_{\mathrm{sep}}=2mgL.
$$

This energy defines a constant-energy curve in phase space called the separatrix. To obtain its mathematical form, set the total energy equal to the separatrix energy:

$$
\frac{1}{2}mL^2\omega^2+mgL(1-\cos\theta)=2mgL.
$$

Rearranging for $\omega$ yields

$$
\omega^2=\frac{2g}{L}(1+\cos\theta).
$$

Using

$$
1+\cos\theta=2\cos^2\left(\frac{\theta}{2}\right),
$$

the separatrix can be written as

$$
\omega = \pm 2\sqrt{\frac{g}{L}}\cos\left(\frac{\theta}{2}\right).
$$

This curve forms the boundary between the two types of motion. For $E<E_{\mathrm{sep}}$, the pendulum oscillates back and forth, while for $E>E_{\mathrm{sep}}$, it has enough energy to rotate continuously.

The connection between energy and phase-space geometry becomes especially important when damping is introduced. As the pendulum loses energy, its trajectory can cross the separatrix and transition from rotation to oscillation.

## Numerical Methods

The pendulum equations do not generally have a simple closed-form solution, so its dynamics are computed numerically. This project compares Euler's Method with Euler-Cromer, focusing not only on numerical accuracy but on how each method affects the long-term behavior and phase-space geometry of the system.

### Euler's Method

Euler's Method was introduced and tested in the previous project, [*Scaling Laws in Projectile Motion with Quadratic Drag*](https://github.com/rohitkb7782/Scaling-Laws-in-Projectile-Motion-with-Quadratic-Drag), where its first-order convergence was examined against the analytical solution for ideal projectile motion.

For the pendulum, the equations

$$
\dot{\theta}=\omega,
\qquad
\dot{\omega}=-\frac{g}{L}\sin\theta
$$

are integrated using

$$
\theta_{n+1}=\theta_n+\omega_n\Delta t,
$$

$$
\omega_{n+1}
=\omega_n-\frac{g}{L}\sin(\theta_n)\Delta t.
$$

For an ideal pendulum, the true motion remains bounded and its mechanical energy is conserved. Over long integrations, however, Euler's Method systematically introduces energy into the numerical solution, causing the amplitude to grow and the phase-space trajectory to spiral outward.

### Euler-Cromer

Euler-Cromer modifies Euler's Method by updating the angular velocity before using it to update the angle:

$$
\omega_{n+1}
=\omega_n-\frac{g}{L}\sin(\theta_n)\Delta t,
$$

$$
\theta_{n+1}
=\theta_n+\omega_{n+1}\Delta t.
$$

This small change produces substantially different long-term behavior. For oscillatory systems, Euler-Cromer keeps the trajectory bounded and preserves the qualitative structure of phase space much more effectively than standard Euler integration.

### Comparing Numerical Behavior

For a short simulation, both methods can produce trajectories that appear reasonable. Over many periods, however, their differences accumulate and become visible in the system's energy and phase-space geometry.

This makes the pendulum a useful test of long-term qualitative behavior. The important question is not only how closely a numerical trajectory follows the exact solution at a given time, but whether it preserves the fundamental structure of the dynamics: bounded oscillations, approximately conserved energy, and closed phase-space trajectories.

The comparison therefore asks whether a numerical method reproduces the character of the dynamics over long times, not simply the motion over a short interval.

## Results

The first two results use the linearized pendulum rather than the full nonlinear equation. This provides a simpler mathematical setting in which to isolate the behavior of the numerical methods before introducing nonlinear phase-space geometry.

### 1. Euler vs. Euler-Cromer — $\theta(t)$ and Energy

The first comparison shows the angular displacement and mechanical energy of the linearized pendulum over many oscillation periods.

![Euler vs. Euler-Cromer](files/euler_vs_euler-cromer.png?raw=true)

**Figure 1.** *Euler's Method and Euler-Cromer compared through angular displacement and mechanical energy for the linearized pendulum.*

Although both methods initially produce similar motion, their long-term behavior quickly diverges. With Euler's Method, the amplitude grows continuously, accompanied by rapid growth in the numerical energy. Euler-Cromer's amplitude remains approximately constant, while its energy stays bounded and oscillates around the expected value.

Thus, over long times, Euler's Method causes the simulated oscillator to gain energy and grow in amplitude, while Euler-Cromer maintains bounded oscillatory motion.

### 2. Euler vs. Euler-Cromer — Phase Space

The difference becomes even clearer in phase space. For the linearized pendulum,

$$
\ddot{\theta}+\omega_0^2\theta=0,
$$

where

$$
\omega_0=\sqrt{\frac{g}{L}}
$$

is the natural angular frequency.

The Euler and Euler-Cromer updates can be written as matrix transformations of the phase-space state:

$$
\begin{pmatrix}
\theta_{n+1}\\
\omega_{n+1}
\end{pmatrix}
=A
\begin{pmatrix}
\theta_n\\
\omega_n
\end{pmatrix}.
$$

For Euler's Method,

$$
A_{\mathrm{Euler}}=
\begin{pmatrix}
1 & h\\
-h\omega_0^2 & 1
\end{pmatrix},
$$

while for Euler-Cromer,

$$
A_{\mathrm{EC}}=
\begin{pmatrix}
1-h^2\omega_0^2 & h\\
-h\omega_0^2 & 1
\end{pmatrix}.
$$

Their determinants are

$$
\det(A_{\mathrm{Euler}})
=1+h^2\omega_0^2>1,
$$

while

$$
\det(A_{\mathrm{EC}})=1.
$$

Because the determinant gives the factor by which a two-dimensional transformation scales area, Euler expands phase-space area at every timestep, while Euler-Cromer preserves it.

![Euler vs. Euler-Cromer Phase Space](files/euler_vs_euler-cromer_phase_space.png?raw=true)

**Figure 2.** *Phase-space trajectories produced by Euler's Method and Euler-Cromer for the linearized pendulum.*

This connects directly to the energy behavior in Figure 2. For the linearized pendulum, the mass-normalized energy is

$$
E=\frac12\omega^2+\frac12\omega_0^2\theta^2.
$$

Constant-energy trajectories are ellipses,

$$
\frac{\theta^2}{a^2}
+
\frac{\omega^2}{b^2}
=1,
$$

with

$$
a=\frac{\sqrt{2E}}{\omega_0},
\qquad
b=\sqrt{2E}.
$$

Their enclosed area is therefore

$$
A=\pi ab=\frac{2\pi E}{\omega_0},
$$

so

$$
A\propto E.
$$

The outward expansion of Euler's phase-space trajectory therefore corresponds directly to its artificial growth in energy, while Euler-Cromer's area-preserving update keeps the trajectory bounded.

### 3. Phase Space of the Nonlinear Pendulum

The phase-space geometry changes significantly as the pendulum's amplitude increases. The figure shows several trajectories of the nonlinear pendulum, beginning with small oscillations near the stable equilibrium and progressing toward the separatrix and rotational regime.

![Pendulum Phase Space](files/pendulum_phase_space.png?raw=true)

**Figure 3.** *Phase-space trajectories of the nonlinear pendulum at increasing energies, showing the transition from small oscillations to large-amplitude motion, the separatrix, and rotational motion.*

At small amplitudes, the trajectory is approximately elliptical and closely resembles the phase-space orbit predicted by the linearized pendulum. As the amplitude increases, however, the nonlinear $\sin\theta$ term becomes increasingly important. The orbit becomes distorted, with the top and bottom portions developing progressively sharper corners as the trajectory approaches the separatrix.

The separatrix marks the boundary between two qualitatively different regimes of motion. Inside it, the pendulum oscillates around the stable equilibrium, represented by the black point at the center of the figure. Outside it, the pendulum has enough energy to rotate continuously rather than reverse direction. The sinusoidal-looking trajectory outside the separatrix therefore represents a different dynamical regime, not simply a larger oscillation.

The increasing distortion near the separatrix is connected to the unstable equilibrium at the top of the pendulum's motion. For a phase-space trajectory $(\theta(t),\omega(t))$, a stationary point occurs when both components of its phase-space velocity vanish:

$$
\frac{d\theta}{dt}=\omega=0,
\qquad
\frac{d\omega}{dt}=\dot{\omega}=0.
$$

For the pendulum, these are precisely the conditions for equilibrium. At the unstable equilibrium, nearby trajectories do not form closed orbits around the point. Instead, the separatrix approaches and departs from it, producing the cusp-like structure visible in the limiting phase-space geometry.

This gives the phase-space picture a direct dynamical interpretation: closed trajectories around the stable equilibrium represent oscillations, the separatrix is the boundary between regimes, and trajectories outside it represent continuous rotation. The geometry changes continuously with energy, but the type of motion changes qualitatively when the separatrix is crossed.

### 4. Damping and the Transition from Rotation to Oscillation

The next animation follows a damped pendulum as it loses energy and crosses from rotational motion into oscillation. The three panels show the same dynamics from complementary perspectives: the physical pendulum and its velocity vector on the left, the phase-space trajectory on the right, and the total energy at the bottom.

![Animation of Damped Pendulum, Phase Space, and Energy](files/damped_phase_space.gif?raw=true)

**Figure 4.** *Damped pendulum transitioning from rotation to oscillation. The left panel shows the physical pendulum and velocity vector, the right panel shows its phase-space trajectory and separatrix, and the bottom panel shows the ktotal energy.*

The pendulum begins above the separatrix energy and therefore has enough energy to rotate continuously. It completes two rotations while gradually losing energy through damping. As the total energy decreases toward

$$
E_{\mathrm{sep}}=2mgL,
$$

the phase-space trajectory approaches the separatrix. Once the energy falls below this threshold, the pendulum can no longer complete another rotation and enters the oscillatory regime.

The transition is visible simultaneously in all three panels. In the physical view, continuous rotation gives way to back-and-forth motion. In phase space, the trajectory crosses the separatrix and becomes a closed oscillatory orbit around the stable equilibrium. In the energy plot, the total energy falls through the separatrix energy at the same point in time.

The animation therefore makes the connection between energy, phase-space geometry, and physical motion explicit: damping changes the energy of the system, and the resulting crossing of the separatrix changes the qualitative character of its motion.


## Stroboscopic Sampling

Introduce stroboscopic maps as discrete samples of a continuous phase-space trajectory:

$$
\mathbf{x}_n=\mathbf{x}(nT_s).
$$

### 4. Commensurability and Stroboscopic Phase Drift

Compare exact commensurability with slight detuning:

$$
T_s=\frac{T_0}{3}
$$

versus

$$
\omega_s=3.05\omega_0.
$$

Show how exact commensurability produces a repeating finite set of stroboscopic points, while slight detuning produces accumulating phase drift.

### 5. Amplitude-Dependent Period and Stroboscopic Alignment

Show how damping changes the nonlinear pendulum's amplitude and therefore its period. Explain how a fixed sampling interval can initially be mismatched with the pendulum's phase but become increasingly aligned as the amplitude decreases.

## Key Findings

* Euler and Euler-Cromer produce qualitatively different long-term behavior for oscillatory systems.
* Phase space makes numerical artifacts and energy behavior more apparent than angle-versus-time plots alone.
* The small-angle approximation produces qualitatively different phase-space geometry from the full nonlinear pendulum at large amplitudes.
* The separatrix separates oscillatory and rotational motion.
* Damping can move the pendulum from rotational motion into oscillatory motion by reducing its mechanical energy below the separatrix energy.
* Stroboscopic sampling converts continuous phase-space trajectories into discrete geometric structures that reveal commensurability and phase drift.
* Because the nonlinear pendulum's period depends on amplitude, damping can change the relationship between the pendulum and a fixed stroboscopic sampling interval.

## Project Structure

```text
Pendulum_Phase_Space/
├── main.py
├── physics.py
├── solvers.py
├── animations.py
├── images/
├── requirements.txt
└── README.md
```

## Requirements

* Python 3
* NumPy
* Matplotlib

## Running the Project

### 1. Clone the repository

```bash
git clone [repository-url]
cd [repository-name]
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

The program generates the phase-space plots, numerical comparisons, and animations described above.

## Future Improvements

* Compare the custom numerical integrators with higher-order methods such as RK4.
* Investigate the exact nonlinear period using elliptic integrals.
* Analyze the modified energy associated with Euler-Cromer.
* Introduce a genuinely nonzero periodic driving force.
* Extend the stroboscopic analysis to periodically driven nonlinear dynamics.
* Explore period-doubling and chaotic regimes.

## Conclusion

This project uses the pendulum as a simple dynamical system for investigating how motion can be understood through phase-space geometry.

The comparison of Euler's Method and Euler-Cromer demonstrates that numerical integration can affect not only quantitative accuracy but also the qualitative geometry of an oscillatory system. The transition from the linearized to the nonlinear pendulum then reveals how the approximation $\sin\theta\approx\theta$ changes the structure of phase space, including the appearance of a separatrix separating oscillatory and rotational motion.

Damping provides a way to observe transitions between these regimes, while stroboscopic sampling provides a discrete view of continuous motion. Exact commensurability produces repeating phase-space structures, slight detuning produces accumulating phase drift, and the amplitude-dependent period of the nonlinear pendulum can change its relationship with a fixed sampling interval as the system loses energy.

The central theme of the project is therefore not simply modeling a pendulum, but understanding how **numerical methods, nonlinear dynamics, and phase-space representations reveal different aspects of the same physical system**.

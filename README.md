# Exploring Pendulum Dynamics Through Phase Space

Rather than asking only *where is the pendulum at a given time?*, phase space allows us to ask *what states can the pendulum occupy, and how does it move between them?*

This computational physics project uses the pendulum as a simple dynamical system for exploring these questions. It begins with a comparison of Euler's Method and Euler-Cromer, then uses phase-space geometry to examine the transition from linear to nonlinear behavior, the boundary between oscillation and rotation, and the effects of damping. Finally, stroboscopic sampling examines what happens when temporal information is reintroduced into the phase-space representation, revealing how the relationship between a fixed sampling interval and the pendulum's period produces structures that are difficult to see in the continuous trajectory alone.

![Phase space](files/stroboscope_pendulum.png?raw=true)

*Stroboscopic sampling of a damped nonlinear pendulum, showing the changing phase relationship between the pendulum and a fixed sampling interval.*

## Motivation

### Phase Space

A time-domain plot shows how a variable changes with time, but it does not always make the structure of that motion easy to see. Phase space instead represents the state of a system through its position and velocity. For the pendulum, this state is

$$
(\theta,\omega),
$$

where $\theta$ is the angular displacement and $\omega=\dot{\theta}$ is the angular velocity.

This representation turns the dynamics into geometry. Periodic oscillations form closed trajectories, rotational motion follows a distinct class of trajectories, and the boundary between these regimes appears as a separatrix. It also makes the effects of numerical error, damping, and nonlinear dynamics directly visible in the geometry of the trajectory.

For this project, phase space is therefore more than an alternative way to plot the motion: it provides a way to connect the pendulum's state, energy, and long-term behavior in a single representation.

A phase-space trajectory, however, does not directly show how the system's motion relates to an external timescale. Although the trajectory is generated through time evolution, a static phase-space plot does not explicitly indicate when different states are visited. Stroboscopic sampling provides a way to examine this relationship by recording the phase-space state at regular intervals and comparing the sampling interval with the pendulum's period.

### The Pendulum

The pendulum is a simple system that contains several important features of nonlinear dynamics. At small angles, it can be approximated as a linear harmonic oscillator through

$$
\sin\theta \approx \theta,
$$

providing a direct comparison between linear and nonlinear behavior within the same physical system.

At larger amplitudes, nonlinear effects distort the phase-space trajectories and produce a separatrix between oscillatory and rotational motion. Damping adds another layer by causing the system to lose energy and potentially move between these dynamical regimes.

The pendulum therefore provides a compact setting for exploring how numerical methods, nonlinearity, energy, damping, and the relationship between intrinsic and external timescales shape the geometry of a dynamical system.

### Research Question

> **How does phase-space geometry reveal the numerical and dynamical behavior of a pendulum, and how does stroboscopic sampling reveal the relationship between its changing timescale and a fixed temporal reference?**

This question guides the project from numerical integration to phase-space analysis, beginning with the behavior of different numerical methods, then examining nonlinear geometry and damping, and finally using stroboscopic sampling to investigate how the pendulum's changing period relates to a fixed sampling interval.

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
\ddot{\theta}+\frac{b}{m}\dot{\theta}+\frac{g}{L}\sin\theta=0,
$$

where $b$ is the linear viscous damping coefficient.

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

Because the absolute value of the determinant gives the factor by which a two-dimensional transformation scales area, Euler expands phase-space area at every timestep, while Euler-Cromer preserves it.

![Euler vs. Euler-Cromer Phase Space](files/euler_vs_euler-cromer_phase_space.png?raw=true)

**Figure 2.** *Phase-space trajectories produced by Euler's Method and Euler-Cromer for the linearized pendulum.*

This connects directly to the energy behavior in Figure 1. For the linearized pendulum, the energy per unit $mL^2$ is

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

Although phase-space area preservation and energy conservation are closely linked here, they are not the same. Euler-Cromer does not conserve the numerical energy exactly at every timestep, but its area-preserving update keeps the trajectory bounded.

The outward expansion of Euler's phase-space trajectory therefore reflects its artificial growth in energy, while Euler-Cromer's area-preserving update keeps the trajectory bounded.

### 3. Phase Space of the Nonlinear Pendulum

The phase-space geometry changes significantly as the pendulum's amplitude increases. The figure shows several trajectories of the nonlinear pendulum, beginning with small oscillations near the stable equilibrium and progressing toward the separatrix and rotational regime.

![Pendulum Phase Space](files/pendulum_phase_space.png?raw=true)

**Figure 3.** *Phase-space trajectories of the nonlinear pendulum at increasing energies, showing the transition from small oscillations to large-amplitude motion, the separatrix, and rotational motion.*

At small amplitudes, the trajectory is approximately elliptical and closely resembles the phase-space orbit predicted by the linearized pendulum. As the amplitude increases, however, the nonlinear $\sin\theta$ term becomes increasingly important. The orbit becomes distorted, with the top and bottom portions developing progressively sharper turns as the trajectory approaches the separatrix.

The separatrix marks the boundary between two qualitatively different regimes of motion. Inside it, the pendulum oscillates around the stable equilibrium, represented by the black point at the center of the figure. Outside it, the pendulum has enough energy to rotate continuously rather than reverse direction. The repeating trajectory outside the separatrix therefore represents a different dynamical regime, not simply a larger oscillation.

The increasing distortion near the separatrix is connected to the unstable equilibrium at the top of the pendulum's motion. For a phase-space trajectory $(\theta(t),\omega(t))$, a stationary point occurs when both components of its phase-space velocity vanish:

$$
\frac{d\theta}{dt}=\omega=0,
\qquad
\frac{d\omega}{dt}=\dot{\omega}=0.
$$

For the pendulum, these are precisely the conditions for equilibrium. At the unstable equilibrium, nearby trajectories do not form closed orbits around the point. Instead, the separatrix approaches and departs from it, producing the sharp turning structure visible in the limiting phase-space geometry.

This gives the phase-space picture a direct dynamical interpretation: closed trajectories around the stable equilibrium represent oscillations, the separatrix is the boundary between regimes, and trajectories outside it represent continuous rotation. The phase-space geometry changes continuously with energy, while crossing the separatrix marks a qualitative change in the type of motion.

### 4. Damping and the Transition from Rotation to Oscillation

The next animation follows a damped pendulum as it loses energy and crosses from rotational motion into oscillation. The three panels show the same dynamics from complementary perspectives: the physical pendulum and its velocity vector on the left, the phase-space trajectory on the right, and the total energy at the bottom.

![Animation of Damped Pendulum, Phase Space, and Energy](files/damped_phase_space.gif?raw=true)

**Figure 4.** *Damped pendulum transitioning from rotation to oscillation. The left panel shows the physical pendulum and velocity vector, the right panel shows its phase-space trajectory and separatrix, and the bottom panel shows the total energy.*

The pendulum begins above the separatrix energy and therefore has enough energy to rotate continuously. It completes two rotations while gradually losing energy through damping. As the total energy decreases toward

$$
E_{\mathrm{sep}}=2mgL,
$$

the phase-space trajectory approaches the separatrix. Once the energy falls below this threshold, the pendulum can no longer complete another rotation and enters the oscillatory regime.

The transition is visible simultaneously in all three panels. In the physical view, continuous rotation gives way to back-and-forth motion. In phase space, the trajectory crosses the separatrix and enters the oscillatory regime, spiraling inward toward the stable equilibrium. In the energy plot, the total energy falls through the separatrix energy at the same point in time.

The animation therefore makes the connection between energy, phase-space geometry, and physical motion explicit: damping changes the energy of the system, and the resulting crossing of the separatrix changes the qualitative character of its motion.

## Stroboscopic Sampling

A phase-space trajectory describes the states visited by the system and the geometry connecting them, but a static plot does not directly indicate how the trajectory is traversed in time. Stroboscopic sampling adds a fixed temporal reference by recording the state of the system at regular intervals,

$$
\mathbf{x}_n=\mathbf{x}(nT_s).
$$

For a periodic system, the resulting pattern depends on the relationship between the sampling interval $T_s$ and the period of the motion. If the two are commensurate, the sampled states repeat after a finite number of steps. If they are not commensurate, the sampling phase drifts from cycle to cycle.

The sampled points therefore do not represent a new dynamical trajectory. Instead, they reveal how the system's motion is traversed relative to a fixed sampling clock. This makes the relationship between the pendulum's intrinsic timescale and an external temporal reference visible in phase space.

### 5. Commensurability and Stroboscopic Phase Drift

A linearized pendulum provides a simple demonstration of how the sampled phase-space pattern depends on the relationship between the sampling interval and the oscillation period. The continuous phase-space trajectory is an ellipse. The sampling interval is deliberately chosen relative to the small-angle period rather than derived from the pendulum dynamics; this controlled choice makes the effects of commensurability and phase drift especially clear. For the top row,

$$
T_s=\frac{T_0}{3},
$$

so three sampling intervals correspond exactly to one oscillation period:

$$
3T_s=T_0.
$$

The sampled states therefore repeat after every three points, producing a triangular pattern in phase space. 

![Stroboscopic Sampling of Linearized Pendulum](files/stroboscope_basics.png?raw=true)

**Figure 5.** *Stroboscopic sampling of a linearized pendulum. The top row shows exact commensurability, with*
$T_s=T_0/3$, *while the bottom row shows slight detuning,*
$T_s=T_0/\sqrt{9.3}$, *producing phase drift.*

For the bottom row, the sampling interval is slightly detuned:

$$
T_s=\frac{T_0}{\sqrt{9.3}}.
$$

The sampling interval is now incommensurate with the pendulum's period, so the sampling phase does not repeat exactly. Instead, the sampled points gradually move around the underlying ellipse, producing the apparent rosette. The continuous pendulum trajectory itself is unchanged; the pattern arises from sampling that trajectory at a fixed interval that does not match its period.

This simple example establishes the mechanism used in the next experiment. There, the sampling interval remains fixed while the nonlinear pendulum's period changes with amplitude, allowing the evolution of the sampling phase relationship to be observed as the pendulum damps.

### 6. Amplitude-Dependent Period and Stroboscopic Alignment

The final stroboscopic experiment uses the damped nonlinear pendulum to show how a changing oscillation period affects a fixed sampling interval. The pendulum is sampled at

$$
T_s=\frac{T_0}{3},
$$

where $T_0$ is the small-angle period.

![Stroboscopic Sampling of Damped Pendulum](files/stroboscope_pendulum.png?raw=true)

**Figure 6.** *Stroboscopic sampling of a damped nonlinear pendulum. As damping reduces the amplitude, the nonlinear period approaches the small-angle period, causing the ratio*
$T(\theta_{max})/T_s$ *to converge toward 3 and reducing the phase drift visible in both phase space and the angle-versus-time plot.*

At the beginning of the simulation, the pendulum has a large amplitude, so its nonlinear period is longer than the small-angle period:

$$
T(\theta_{\max})>T_0.
$$

Since the sampling interval is fixed at

$$
T_s=\frac{T_0}{3},
$$

the initial ratio between the pendulum's period and the sampling interval satisfies

$$
\frac{T(\theta_{\max})}{T_s}>3.
$$

The sampling therefore does not initially correspond to exactly three samples per oscillation. This mismatch causes the sampled phase-space points to drift from one cycle to the next, producing triangular patterns that gradually rotate around the underlying trajectory. The angle-versus-time plot shows the same effect as the sampling lines progressively shift relative to the oscillation.

As damping reduces the oscillation amplitude, the nonlinear period approaches the small-angle period:

$$
T(\theta_{\max})\rightarrow T_0.
$$

Consequently, the ratio of the pendulum's period to the sampling interval approaches

$$
\frac{T(\theta_{\max})}{T_s}
\rightarrow
\frac{T_0}{T_0/3}
=3.
$$

Thus, the stroboscopic sampling progressively approaches the condition of exactly three samples per oscillation. As this ratio converges toward 3, the phase drift decreases and the successive triangular patterns become increasingly aligned with one another.

The sampling does not alter the pendulum's dynamics or synchronize its motion. Instead, it reveals the changing relationship between the pendulum's amplitude-dependent period and the fixed sampling interval. The gradual convergence of

$$
\frac{T(\theta_{\max})}{T_s}\rightarrow3
$$

therefore provides a geometric signature of the pendulum's changing timescale as damping reduces its amplitude.

## Key Findings

* Euler's Method introduces systematic energy growth in long integrations of oscillatory systems, while Euler-Cromer preserves bounded phase-space motion much more effectively.
* Phase-space geometry makes the qualitative effects of numerical error visible through the expansion or boundedness of trajectories.
* The linearized pendulum accurately describes small-amplitude motion, but nonlinear effects increasingly distort the phase-space trajectories at larger amplitudes.
* The separatrix, corresponding to the critical energy $E_{\mathrm{sep}}=2mgL$, separates oscillatory motion from continuous rotation.
* Damping causes the pendulum to lose energy and can drive a transition from rotational motion to oscillation as the trajectory crosses the separatrix.
* Stroboscopic sampling reveals how the pendulum's motion relates to a fixed sampling timescale: commensurate periods produce repeating patterns, while mismatched periods produce phase drift.
* Because the nonlinear period depends on amplitude, damping changes this phase relationship over time as the pendulum approaches the small-angle regime.

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
* Investigate the phase-space structure of a periodically driven pendulum.
* Extend the stroboscopic analysis to periodically driven nonlinear dynamics.
* Explore period-doubling and chaotic regimes.

## Conclusion

This project uses the pendulum as a simple dynamical system for investigating how numerical methods, phase-space geometry, nonlinearity, and damping shape our understanding of motion.

The comparison of Euler's Method and Euler-Cromer shows that numerical integration affects not only quantitative accuracy but also the qualitative structure of an oscillatory system. Euler's Method introduces artificial energy growth over long integrations, while Euler-Cromer keeps the trajectory bounded and preserves the structure of phase space more effectively. Moving from the linearized to the nonlinear pendulum then shows how the approximation $\sin\theta\approx\theta$ breaks down at larger amplitudes, producing distorted trajectories and a separatrix between oscillatory and rotational motion.

Damping makes this phase-space structure dynamic. As the pendulum loses energy, its trajectory approaches and crosses the separatrix, producing a transition from rotational motion to oscillation around the stable equilibrium.

Stroboscopic sampling extends this phase-space analysis by introducing a fixed temporal reference. A continuous phase-space trajectory describes the geometry of the motion, but does not directly show how that motion is traversed relative to an external clock. When the sampling interval is commensurate with the pendulum's period, the sampled states repeat; when the two timescales are mismatched, the sampling phase drifts. For the nonlinear damped pendulum, this relationship changes naturally because its period depends on amplitude and the amplitude decreases with damping. The choice of sampling interval in this experiment is deliberate rather than physically preferred; it provides a controlled way to expose the changing relationship between the pendulum's intrinsic period and an external temporal reference.

The central theme of the project is therefore not simply modeling a pendulum, but examining how different methods of representation reveal different aspects of its dynamics. Numerical methods determine how faithfully the dynamics are reproduced, phase space reveals their geometric structure, and stroboscopic sampling reveals how that structure relates to a fixed temporal reference.

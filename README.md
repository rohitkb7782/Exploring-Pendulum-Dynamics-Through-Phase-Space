# Exploring Pendulum Dynamics Through Phase Space

A computational physics project investigating how phase space can be used to visualize and interpret the dynamics of a pendulum. The project begins with numerical integration and a comparison of Euler's Method and Euler-Cromer, then uses phase-space geometry to examine the transition from linear to nonlinear behavior, the effects of damping, and the structure revealed by stroboscopic sampling.

![Phase space](files/stroboscope_pendulum.png?raw=true)

**Figure 1.** [Opening figure/collage to be selected.]

## Motivation

### Phase Space

Motion is often represented by plotting a variable such as position or angle against time. While this shows how a system evolves, it can hide the underlying structure of that motion. Phase space provides a different perspective by representing the state of a system through its position and velocity. For the pendulum, this state is

$$
(\theta,\omega),
$$

where $\theta$ is the angular displacement and $\omega$ is the angular velocity.

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

This question guides the project from numerical simulation to phase-space analysis, using computation not simply to model the pendulum's motion, but to reveal the structure of its dynamics.

## Mathematical Model

### Pendulum Equation

Consider a pendulum of length $L$ and mass $m$, with angular displacement $\theta$ measured from the downward vertical. In the absence of damping or external forcing, its equation of motion is

$$
\ddot{\theta}+\frac{g}{L}\sin\theta=0,
$$

where $g$ is the acceleration due to gravity.

The $\sin\theta$ term makes the pendulum a nonlinear dynamical system. Writing the equation as a first-order system,

$$
\dot{\theta}=\omega,
$$

$$
\dot{\omega}=-\frac{g}{L}\sin\theta,
$$

gives the state variables used to construct the phase-space trajectories:

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
K=\frac{1}{2}mL^2\dot{\theta}^2
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
\frac{1}{2}mL^2\omega^2+mgL(1-\cos\theta)=2mgL
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

The pendulum equations do not generally have a simple closed-form solution, so its dynamics are computed numerically. This project compares **Euler's Method** with **Euler-Cromer**, focusing not only on numerical accuracy but on how each method affects the long-term behavior and phase-space geometry of the system.

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
\omega_{n+1}=
\omega_n-\frac{g}{L}\sin(\theta_n)\Delta t.
$$

For an ideal pendulum, the true motion remains bounded and its mechanical energy is conserved. Over long integrations, however, Euler's Method systematically introduces energy into the numerical solution, causing the amplitude to grow and the phase-space trajectory to spiral outward.

### Euler-Cromer

Euler-Cromer modifies Euler's Method by updating the angular velocity before using it to update the angle:

$$
\omega_{n+1}=
\omega_n-\frac{g}{L}\sin(\theta_n)\Delta t,
$$

$$
\theta_{n+1}=
\theta_n+\omega_{n+1}\Delta t.
$$

This small change produces substantially different long-term behavior. For oscillatory systems, Euler-Cromer keeps the trajectory bounded and preserves the qualitative structure of phase space much more effectively than standard Euler integration.

### Comparing Numerical Behavior

For a short simulation, both methods can produce trajectories that appear reasonable. Over many periods, however, their differences accumulate and become visible in the system's energy and phase-space geometry.

This makes the pendulum a useful test of long-term qualitative behavior. The important question is not only how closely a numerical trajectory follows the exact solution at a given time, but whether it preserves the fundamental structure of the dynamics: bounded oscillations, approximately conserved energy, and closed phase-space trajectories.

The comparison therefore asks whether a numerical method reproduces the character of the dynamics over long times, not simply the motion over a short interval.

## Results

### 1. Numerical Methods and Long-Term Behavior

Compare Euler and Euler-Cromer through angle, energy, and phase space.

### 2. Phase-Space Geometry of the Linear and Nonlinear Pendulum

Compare the linearized and nonlinear equations at large amplitude, emphasizing distorted orbits and the separatrix.

### 3. Damping and the Transition from Rotation to Oscillation

Use the synchronized animation of the pendulum, phase space, and kinetic/potential/total energy to show the loss of energy and crossing of the separatrix.

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

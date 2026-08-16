import numpy as np

def linear_derivative(state, time, consts):
    '''
    Takes in the position and velocity of a mass on a spring, packaged in one vector, and the current time.
    Returns its velocity and acceleration, packaged in one vector.

    Parameters
    ----------
    state: a two-element tuple or array (theta, omega) representing the current angle and angular velocity state
    time: a float representing the current time
    consts: a tuple of physical constants (gravity, pendulum length, mass)

    Returns
    -------
    derivative_of_state: a two-element array (omega, alpha) representing the current angular velocity and angular acceleration state
    '''
    #%% Set constants.
    g, L, m = consts                       # gravitational acceleration     [m/s^2]

    #%% Unpack the vector's components.
    theta = state[0]
    omega = state[1]

    #%% Compute the derivatives.
    derivative_of_state = np.zeros(2)                    # Create a list to store derivatives.
    derivative_of_state[0] = omega                       # angular velocity
    derivative_of_state[1] = -g/L * theta                # angular acceleration
    return derivative_of_state

def pendulum_derivative(state, time, consts):
    '''
    Takes in the position and velocity of a mass on a spring, packaged in one vector, and the current time.
    Returns its velocity and acceleration, packaged in one vector.

    Parameters
    ----------
    state: a two-element tuple or array (theta, omega) representing the current angle and angular velocity state
    time: a float representing the current time
    consts: a tuple of physical constants (gravity, pendulum length, mass)

    Returns
    -------
    derivative_of_state: a two-element array (omega, alpha) representing the current angular velocity and angular acceleration state
    '''
    #%% Set constants.
    g, L, m = consts                       # gravitational acceleration     [m/s^2]

    #%% Unpack the vector's components.
    theta = state[0]
    omega = state[1]

    #%% Compute the derivatives.
    derivative_of_state = np.zeros(2)                    # Create a list to store derivatives.
    derivative_of_state[0] = omega                       # angular velocity
    derivative_of_state[1] = -g/L * np.sin(theta)        # angular acceleration
    return derivative_of_state


def pendulum_drag_derivative(state, time, consts):
    '''
    This model includes air resistance.
    Takes in the position and velocity of a mass on a spring, packaged in one vector, and the current time.
    Returns its velocity and acceleration, packaged in one vector.

    Parameters
    ----------
    state: a two-element tuple or array (theta, omega) representing the current angle and angular velocity state
    time: a float representing the current time
    consts: a tuple of physical constants (gravity, pendulum length, mass, air resistance)

    Returns
    -------
    derivative_of_state: a two-element array (omega, alpha) representing the current angular velocity and angular acceleration state
    '''
    #%% Set constants.
    g, L, m, b = consts                       # gravitational acceleration     [m/s^2]

    #%% Unpack the vector's components.
    theta = state[0]
    omega = state[1]

    #%% Compute the derivatives.
    derivative_of_state = np.zeros(2)                              # Create a list to store derivatives.
    derivative_of_state[0] = omega                                 # angular velocity
    derivative_of_state[1] = -g/L * np.sin(theta) - b*omega        # angular acceleration
    return derivative_of_state
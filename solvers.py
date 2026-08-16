import numpy as np

def euler_solver(derivative_function, initial_state, times, consts):
    '''
    Uses Euler's method to find the solution to a differential equation at specified timesteps
    
    Parameters
    ----------
    update_function(state, time): a function that inputs the current state and time and outputs the derivative
    initial_state: a 1D tuple or array encoding the initial conditions
    times: a 1D array of times at which the states are to be computed

    Returns
    -------
    states: a 1D array the same size as (times), with the states at each corresponding time
    '''
    #%% Create an array to store states at specified timesteps.
    states = np.zeros(( len(times), len(initial_state) ))
    states[0] = initial_state

    #%% Fill the states array with estimates using Euler's method.
    for i in range(len(times) - 1):
        slope = derivative_function(states[i], times[i], consts)     # Get the state's derivative at a specified time
        dt = times[i+1] - times[i]
        states[i+1] = states[i] + slope * dt                         # Use Euler's method to determine the next state
        
    return states


def euler_cromer_solver(derivative_function, initial_state, times, consts):
    '''
    Uses the Euler-Cromer method to find the solution to a differential equation at specified timesteps.
    Euler-Cromer solves a system of two first order equations for position and velocity.
    Euler-Cromer conserves energy, as opposed to Euler's method which tends to add energy.
    
    Parameters
    ----------
    derivative_function(state, time): a function that inputs the current state and time and outputs the derivative
    initial_state: a 2-element tuple or array encoding the initial conditions: (initial_position, initial_velocity)
    times: a 1D array of times at which the states are to be computed

    Returns
    -------
    states: a 2D array with shape (times.shape, 2), with the states at each corresponding time. 
            the element states[i] is (ith_position, ith_velocity)
    '''
    #%% Create an array to store states at specified timesteps.
    states = np.zeros(( len(times), len(initial_state) ))
    states[0] = initial_state

    #%% Fill the states array with estimates using Euler-Cromer method.
    for i in range(len(times) - 1):
        _, a_this_step = derivative_function(states[i], times[i], consts)     # Calculate the acceleration at this step
        dt = times[i+1] - times[i]
        v_next_step = states[i,1] + a_this_step * dt                          # Calculate the velocity at the next step
        
        states[i+1,0] = states[i,0] + v_next_step * dt                        # Enter the position at the next step into the states array
        states[i+1,1] = v_next_step                                           # Enter the velocity at the next step into the states array
        
    return states
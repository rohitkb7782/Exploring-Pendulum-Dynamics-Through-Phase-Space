def get_peaks(values):
    '''
    Returns two lists: the indexes of successive maxima of a set of values, and the maxima themselves.

    Params
    ------
    values: a list of values with multiple maxima

    Returns
    -------
    peak_indexes: a list of indexes of successive maxima of values
    peak_values: a list of the successive maxima themselves
    '''
    # Record the indexes at which the value reaches its maximum
    peak_indexes = []
    peak_values = []
    for i in range(1,len(values)-1):
        if values[i] > values[i+1] and values[i] > values[i-1]:
            peak_indexes.append(i)
            peak_values.append(values[i])
    return peak_indexes, peak_values

def get_periods(times, values):
    '''
    Returns a list containing the time separations between successive maxima of a set of values.
    If the period of your system is constant with respect to time, 
    take the mean of the outputted list to get the system's period.

    Params
    ------
    times: a list of times
    values: a list of values with multiple maxima; value[i] corresponds to times[i]

    Returns
    -------
    periods: a list of time separations between successive maxima of values
    '''
    # Record the indexes at which the value reaches its maximum
    peak_indexes, _ = get_peaks(values)

    # Record the times between successive maximums as a list of periods
    periods = []
    for i in range(len(peak_indexes)-1):
        periods.append(times[peak_indexes[i+1]] - times[peak_indexes[i]])
    return periods
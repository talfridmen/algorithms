import random  # might be useful ;)

def monte_carlo(reps):
    import numpy as np # going to do everything in one line to make your eyes hurt
    return 4*np.count_nonzero(np.sum(np.square(np.random.rand(reps,2)), axis=1) <= 1.0)/reps
    # First we create an array with reps rows and 2 columns of random numbers between 0,1.0 : np.random.rand(reps,2)
    # next we square all elements : np.square()
    # next we sum all columns in each row : no.sum(array, axis=1) -> our 2D array is now 1D with each element is sum(square)
    # next we count all elemnts that return True for the condition <= 1.0, using the fact True == 1 and False == 0 : np.count_nonzero(array <= 1.0)


import random  # might be useful ;)

def monte_carlo(reps):
    counter = 0
    for i in range(1,reps):
        x,y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            counter += 1
    return 4*counter/reps

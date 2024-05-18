import random  # might be useful ;)

def monte_carlo(reps):
    in_circle = 0
    for i in range(reps):
        x, y = random.random(), random.random()
        if (x ** 2 + y ** 2) ** 0.5 <= 1:
            in_circle += 1
    return 4 * in_circle / reps

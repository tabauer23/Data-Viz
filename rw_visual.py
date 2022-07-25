import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active. 
while True:
    # Make a new random walk, and plot the points.
    rw=RandomWalk(50000)
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk (y/n)?: ").lower()
    if not keep_running.startswith('y'):
        break
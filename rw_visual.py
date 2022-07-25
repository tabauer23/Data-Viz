import matplotlib.pyplot as plt
from random_walk2 import RandomWalk

# Keep making new walks, as long as the program is active. 
while True:
    # Make a new random walk, and plot the points.
    rw=RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    # Emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    keep_running = input("Make another walk (y/n)?: ").lower()
    if not keep_running.startswith('y'):
        break
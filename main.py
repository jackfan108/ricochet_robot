import matplotlib.pyplot as plt
import numpy as np
import random

LINEWIDTH = 3
COLOR = 'black'

# randomly generates a point and chooses one of 4 orientations to extend 2 walls
def generate_corner(x1, y1, x2, y2):
    x = random.randint(x1+1, x2-1)
    y = random.randint(y1+1, y2-1)
    n = random.random()
    if n <= 0.25:
        plt.plot([x, x+1], [y, y], linewidth=LINEWIDTH, color=COLOR)
        plt.plot([x, x], [y, y-1], linewidth=LINEWIDTH, color=COLOR)
    elif n <= 0.5:
        plt.plot([x, x], [y, y+1], linewidth=LINEWIDTH, color=COLOR)
        plt.plot([x, x+1], [y, y], linewidth=LINEWIDTH, color=COLOR)
    elif n <= 0.75:
        plt.plot([x, x-1], [y, y], linewidth=LINEWIDTH, color=COLOR)
        plt.plot([x, x], [y, y+1], linewidth=LINEWIDTH, color=COLOR)
    else:
        plt.plot([x, x], [y, y-1], linewidth=LINEWIDTH, color=COLOR)
        plt.plot([x, x-1], [y, y], linewidth=LINEWIDTH, color=COLOR)



def generate_target():
    x = random.randint(0, 15)
    y = random.randint(0, 15)
    return (x+0.5, y+0.5)

def generate_color():
    return random.choice(['red', 'green', 'blue', 'yellow'])

if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)

    # draw the boarder
    plt.plot([0, 0], [16, 0], linewidth=LINEWIDTH, color=COLOR)
    plt.plot([16, 0], [16, 16], linewidth=LINEWIDTH, color=COLOR)
    plt.plot([16, 16], [0, 16], linewidth=LINEWIDTH, color=COLOR)
    plt.plot([0, 16], [0, 0], linewidth=LINEWIDTH, color=COLOR)

    # draw the central 2x2 square
    plt.plot([7, 7], [7, 9], linewidth=LINEWIDTH, color=COLOR)
    plt.plot([7, 9], [9, 9], linewidth=LINEWIDTH, color=COLOR)
    plt.plot([9, 9], [9, 7], linewidth=LINEWIDTH, color=COLOR)
    plt.plot([9, 7], [7, 7], linewidth=LINEWIDTH, color=COLOR)

    # generate corners in each quadrant
    corner_count = 7
    for _ in range(corner_count):
        generate_corner(0, 0, 8, 8)
        generate_corner(0, 8, 8, 16)
        generate_corner(8, 8, 16, 16)
        generate_corner(8, 0, 16, 8)

    plt.title('Ricochet Robots')
    plt.grid(True)

    # draw the full grid in increment of 1
    minor_ticks = np.arange(0, 16, 1)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='minor', alpha=0.4)

    for _ in range(17):
        plt.scatter(*generate_target(), color=generate_color(), label='Point', s=100)

    plt.show()

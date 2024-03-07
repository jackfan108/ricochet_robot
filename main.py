import matplotlib.pyplot as plt
import numpy as np
import random

LINEWIDTH = 3

def generate_wall(x1, y1, x2, y2):
    x = random.randint(x1+1, x2-1)
    y = random.randint(y1+1, y2-1)
    n = random.random()
    if n <= 0.25:
        return ([x, x+1], [y, y])
    elif n <= 0.5:
        return ([x, x], [y, y+1])
    elif n <= 0.75:
        return ([x, x-1], [y, y])
    else:
        return ([x, x], [y, y-1])

def generate_target():
    x = random.randint(0, 15)
    y = random.randint(0, 15)
    return (x+0.5, y+0.5)

def generate_color():
    return random.choice(['red', 'green', 'blue', 'yellow'])

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # draw the boarder
    plt.plot([0, 0], [16, 0], linewidth=LINEWIDTH, color='black')
    plt.plot([16, 0], [16, 16], linewidth=LINEWIDTH, color='black')
    plt.plot([16, 16], [0, 16], linewidth=LINEWIDTH, color='black')
    plt.plot([0, 16], [0, 0], linewidth=LINEWIDTH, color='black')

    # draw the central 2x2 square
    plt.plot([7, 7], [7, 9], linewidth=LINEWIDTH, color='black')
    plt.plot([7, 9], [9, 9], linewidth=LINEWIDTH, color='black')
    plt.plot([9, 9], [9, 7], linewidth=LINEWIDTH, color='black')
    plt.plot([9, 7], [7, 7], linewidth=LINEWIDTH, color='black')

    # generate wall_num wall segements in each quadrant
    wall_num = 12
    while wall_num > 0:
        plt.plot(*generate_wall(0, 0, 8, 8), linewidth=LINEWIDTH, color='black')
        plt.plot(*generate_wall(0, 8, 8, 16), linewidth=LINEWIDTH, color='black')
        plt.plot(*generate_wall(8, 8, 16, 16), linewidth=LINEWIDTH, color='black')
        plt.plot(*generate_wall(8, 0, 16, 8), linewidth=LINEWIDTH, color='black')
        wall_num -= 1
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Customizable 2D Grid')
    plt.grid(True)

    # draw the full grid in increment of 1
    minor_ticks = np.arange(0, 16, 1)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='minor', alpha=0.4)

    for _ in range(17):
        plt.scatter(*generate_target(), color=generate_color(), label='Point')

    plt.show()

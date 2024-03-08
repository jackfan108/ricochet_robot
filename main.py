import matplotlib.pyplot as plt
import numpy as np
import random

LINEWIDTH = 3
COLOR = 'black'
BOARD_LEN = 16
BORDER_COORDS = []
wall_coords = set()

# randomly generates a point and chooses one of 4 orientations to extend 2 walls
def generate_corner(x1, y1, x2, y2):
    x = random.randint(x1+1, x2-1)
    y = random.randint(y1+1, y2-1)
    n = random.random()
    if n <= 0.25:
        if is_wall(x, y) or is_wall(x+1, y) or is_wall(x, y-1):
            return generate_corner(x1, y1, x2, y2)
        else:
            plt.plot([x, x+1], [y, y], linewidth=LINEWIDTH, color=COLOR)
            plt.plot([x, x], [y, y-1], linewidth=LINEWIDTH, color=COLOR)
            wall_coords.update([(x, y), (x+1, y), (x, y-1)])
    elif n <= 0.5:
        if is_wall(x, y) or is_wall(x+1, y) or is_wall(x, y+1):
            return generate_corner(x1, y1, x2, y2)
        else:
            plt.plot([x, x], [y, y+1], linewidth=LINEWIDTH, color=COLOR)
            plt.plot([x, x+1], [y, y], linewidth=LINEWIDTH, color=COLOR)
            wall_coords.update([(x, y), (x+1, y), (x, y+1)])
    elif n <= 0.75:
        if is_wall(x, y) or is_wall(x-1, y) or is_wall(x, y+1):
            return generate_corner(x1, y1, x2, y2)
        else:
            plt.plot([x, x-1], [y, y], linewidth=LINEWIDTH, color=COLOR)
            plt.plot([x, x], [y, y+1], linewidth=LINEWIDTH, color=COLOR)
            wall_coords.update([(x, y), (x-1, y), (x, y+1)])
    else:
        if is_wall(x, y) or is_wall(x-1, y) or is_wall(x, y-1):
            return generate_corner(x1, y1, x2, y2)
        else:
            plt.plot([x, x], [y, y-1], linewidth=LINEWIDTH, color=COLOR)
            plt.plot([x, x-1], [y, y], linewidth=LINEWIDTH, color=COLOR)
            wall_coords.update([(x, y), (x-1, y), (x, y-1)])

def is_wall(x, y):
    return (x, y) in wall_coords

def generate_target():
    x = random.randint(0, 15)
    y = random.randint(0, 15)
    return (x+0.5, y+0.5)

def generate_color():
    return random.choice(['red', 'green', 'blue', 'yellow'])

def generate_border_coords():
    bottom = [(x, 0) for x in range(1, BOARD_LEN)]
    top = [(x, BOARD_LEN) for x in range(1, BOARD_LEN)]
    left = [(0, y) for y in range(1, BOARD_LEN)]
    right = [(BOARD_LEN, y) for y in range(1, BOARD_LEN)]
    return bottom + top + left + right

def generate_border_wall():
    x, y = random.choice(BORDER_COORDS)
    if x == 0:
        plt.plot([x, x+1], [y, y], linewidth=LINEWIDTH, color=COLOR)
        return [(x, y), (x+1, y)]
    elif x == BOARD_LEN:
        plt.plot([x, x-1], [y, y], linewidth=LINEWIDTH, color=COLOR)
        return [(x, y), (x-1, y)]
    elif y == 0:
        plt.plot([x, x], [y, y+1], linewidth=LINEWIDTH, color=COLOR)
        return [(x, y), (x, y+1)]
    elif y == BOARD_LEN:
        plt.plot([x, x], [y, y-1], linewidth=LINEWIDTH, color=COLOR)
        return [(x, y), (x, y-1)]
    else:
        print("oops. fucked up on generating border wall")

if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)

    BORDER_COORDS = generate_border_coords()
    wall_coords.update(BORDER_COORDS)

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
    for i in range(7, 10):
        for j in range(7, 10):
            wall_coords.add((i, j))

    # generate border walls
    for _ in range(5):
        wall_coords.update(generate_border_wall())

    # generate corners in each quadrant
    corner_count = 6
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


    # generate targets
    for _ in range(17):
        plt.scatter(*generate_target(), color=generate_color(), label='Point', s=100)

    plt.show()

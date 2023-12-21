from collections import deque
from math import ceil
import time

time_start = time.time()


DIRECTIONS = [(1, 0), (-1 ,0), (0, 1), (0, -1)]

def parse_input():

    file = open("input.txt").read().splitlines()
    grid = []

    for y, line in enumerate(file):

        new_line = []
        for x, char in enumerate(line):

            new_line.append(char)

            if char == 'S':
                start = (y, x)

        grid.append(new_line)


    return grid, start



def get_adjacent(grid, coord):
    global DIRECTIONS

    possible_adjacent = []

    for direction in DIRECTIONS:

        new_coord = (coord[0] + direction[0], coord[1] + direction[1])

        if grid[new_coord[0] % len(grid)][new_coord[1] % len(grid)] != '#':
            possible_adjacent.append(new_coord)

    return possible_adjacent


def steps(grid, start, max_dist):

    queue = deque([(0, start)])
    visited = set()
    total_gardens = 0

    while queue:

        dist, coord = queue.popleft()

        if dist > max_dist:
            break

        if coord in visited:
            continue

        if dist % 2 == max_dist % 2:
            total_gardens += 1


        visited.add(coord)

        for adjacent_coord in get_adjacent(grid, coord):
            if adjacent_coord not in visited:
                queue.append((dist + 1, adjacent_coord))

    
    return total_gardens


# https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
def get_n_term(term):
    global grid, height

    mod = term % height
    term = ceil(term / height)

    a = steps(grid, start, mod)
    b = steps(grid, start, mod + height)
    c = steps(grid, start, mod + (2 * height))

    first_diff_ab = b - a
    first_diff_bc = c - b
    second_diff = first_diff_bc - first_diff_ab

    x = second_diff // 2
    y = first_diff_ab - (3 * x)
    z = a - y - x

    return x*(term**2) + y*term + z



grid, start = parse_input()
height = len(grid)
result = get_n_term(26501365)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
from collections import deque
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


def is_in_bounds(grid, coord):

    return (0 <= coord[0] < len(grid)) and (0 <= coord[1] < len(grid[0]))


def get_adjacent(grid, coord):
    global DIRECTIONS

    possible_adjacent = []

    for direction in DIRECTIONS:

        new_coord = (coord[0] + direction[0], coord[1] + direction[1])

        if is_in_bounds(grid, new_coord):
            if grid[new_coord[0]][new_coord[1]] == '.':
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



grid, start = parse_input()
result = steps(grid, start, 64)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
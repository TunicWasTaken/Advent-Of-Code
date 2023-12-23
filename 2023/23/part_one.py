from collections import deque
import time

time_start = time.time()


DIRECTIONS = [(1, 0), (-1 ,0), (0, 1), (0, -1)]
SLOPES = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def parse_input():

    lines = open("input.txt").read().splitlines()
    
    return [[char for char in line] for line in lines]


def get_adjacent(grid, coord, dist, vis):
    global DIRECTIONS, SLOPES

    height = len(grid)
    width = len(grid[0])
    char = grid[coord[1]][coord[0]]

    if char in SLOPES:

        slope = SLOPES[char]
        new_coord = (coord[0] + slope[0], coord[1] + slope[1])

        if 0 <= new_coord[0] < width and 0 <= new_coord[1] < height and (new_coord[0], new_coord[1], dist - 1) not in vis:
            yield new_coord

    else:
        for direction in DIRECTIONS:

            new_coord = (coord[0] + direction[0], coord[1] + direction[1])

            if 0 <= new_coord[0] < width and 0 <= new_coord[1] < height:
                if grid[new_coord[1]][new_coord[0]] != '#' and (new_coord[0], new_coord[1], dist - 1) not in vis:
                    yield new_coord



def a_long_walk():

    grid = parse_input()
    start_pos = (1, 0)
    queue = deque([(0, start_pos)])
    vis = set()
    dists = {}
    
    while queue:

        dist, pos = queue.popleft()
        state = (pos[0], pos[1], dist)

        if state in vis:
            continue

        vis.add(state)
        dists[pos] = dist

        for adjacent_coord in get_adjacent(grid, pos, dist, vis):
            if (adjacent_coord[0], adjacent_coord[1], dist + 1) not in vis:
                queue.append((dist + 1, adjacent_coord))

        

    return dists[max(dists, key=dists.get)]




result = a_long_walk()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
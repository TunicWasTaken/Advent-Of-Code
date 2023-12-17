import time
import heapq as pq

time_start = time.time()

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)


def parse_input():

    file = open("input.txt")
    grid = {(x,y): int(n) for y, line in enumerate(file.read().splitlines()) for x,n in enumerate(line)}

    return grid


# I hate graphs and I hate implementing Dijkstra
def clumsy_crucible(max_steps):
    
    grid = parse_input()
    queue = [(grid[(1, 0)], RIGHT, RIGHT, 0), (grid[(0, 1)], DOWN, DOWN, 0)]
    visited = set()
    end = max(grid)

    while queue:

        heat_value, (x, y), (dir_x, dir_y), steps = pq.heappop(queue)

        if (x, y) == end:
            return heat_value
        
        if ((x, y), (dir_x, dir_y), steps) in visited:
            continue

        visited.add(((x, y), (dir_x, dir_y), steps))

        if steps < (max_steps - 1) and (x + dir_x, y + dir_y) in grid:

            new_pos = (x + dir_x, y + dir_y)
            pq.heappush(queue, (heat_value + grid[new_pos], new_pos, (dir_x, dir_y), steps + 1))


        l_new_dir_x, l_new_dir_y, r_new_dir_x, r_new_dir_y = dir_y, -dir_x, -dir_y, dir_x
        l_new_pos, r_new_pos = (x + l_new_dir_x, y + l_new_dir_y), (x + r_new_dir_x, y + r_new_dir_y)

        for x, y, pos in zip((l_new_dir_x, r_new_dir_x),(l_new_dir_y, r_new_dir_y),(l_new_pos, r_new_pos)):
            if pos in grid:
                pq.heappush(queue, (heat_value + grid[pos], pos, (x, y), 0))



result = clumsy_crucible(3)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
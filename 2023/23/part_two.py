import sys
import time

sys.setrecursionlimit(10**6)
time_start = time.time()


DIRECTIONS = [(1, 0), (-1 ,0), (0, 1), (0, -1)]
grid = tuple(open("input.txt").read().split('\n'))
height = len(grid)
width = len(grid[0])
    

def get_adjacent(x, y):

    for dir_x, dir_y in DIRECTIONS:

        new_x, new_y = x + dir_x, y + dir_y
 
        if 0 <= new_x < width and 0 <= new_y < height:
                if grid[new_y][new_x] in '^v<>.':
                    yield (new_x, new_y)


def measure(edges, start, head):
    
    count = 1
    while len(edges[head]) == 2:
        count += 1
        next = [n for _, n in edges[head] if n != start][0]
        start, head = (head, next)

    return (count, head)


def trails():

    edges = {}
    for y in range(height):
        for x in range(width):
            if grid[y][x] in '^v<>.':
                edges[(x,y)] = [(1, n) for n in get_adjacent(x, y)]

    new_edges = {}
    for key, val in edges.items():
        if len(val) != 2:
            new_edges[key] = [measure(edges, key, n[1]) for n in val]

    return new_edges


def longest_path_dfs(trails, start, end):
    
    vis = set([start])
    stack = [(start, 0, vis)]
    max_dist = 0

    while stack:
        pos, dist, vis = stack.pop()
        if pos == end:
            max_dist = max(dist, max_dist)

        for d, next in trails[pos]:
            if next not in vis:
                stack.append((next, dist + d, vis | set([next])))

    return max_dist


start = (1, 0)
end = (width - 2, height - 1)
result = longest_path_dfs(trails(), start, end)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
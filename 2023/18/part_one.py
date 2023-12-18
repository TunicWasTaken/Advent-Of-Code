import time

time_start = time.time()


DIRECTIONS = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def lavaduct():
    global DIRECTIONS

    instructions = [[(instruction) for instruction in line.split(" ")] for line in open("input.txt").read().splitlines()]
    pos = (0, 0)
    perimeter = 0
    visited = [(pos)]

    for instruction in instructions:

        direction = DIRECTIONS[instruction[0]]
        steps = int(instruction[1])
        perimeter += steps
        pos = (pos[0] + (steps * direction[0]), pos[1] + (steps * direction[1]))
        visited.append(pos)

    
    area = 0
    for i in range(len(visited) - 1):

        x, y = visited[i]
        xx, yy = visited[i + 1]

        area += x * yy - xx * y
        
    return int((abs(area) >> 1) + (perimeter / 2) + 1)
    


result = lavaduct()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
import time

time_start = time.time()


DIRECTIONS = {'0': (1, 0), '2': (-1, 0), '3': (0, 1), '1': (0, -1)}

def lavaduct():
    global DIRECTIONS

    instructions = [[(instruction) for instruction in line.split(" ")] for line in open("input.txt").read().splitlines()]
    pos = (0, 0)
    perimeter = 0
    visited = [(pos)]

    for instruction in instructions:

        hex_code = instruction[2].split("#")[1]
        direction = DIRECTIONS[hex_code[5]]
        steps = int('0x' + hex_code[0:5], base = 16)
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
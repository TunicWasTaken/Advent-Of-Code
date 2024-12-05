from itertools import product
import time
import re
time_start = time.time()

dirs = [
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

def part_one():
    data = open("input.txt").read().splitlines()
    res = 0

    for x,y in product(range(len(data[0]) - 2), range(len(data) - 2)):
        diagonals = ["".join(data[y + dy][x + dx] for dx, dy in direction) for direction in dirs]
        res += all(re.match(r"MAS|SAM","".join(diagonal)) for diagonal in diagonals)

    return res

        
res = part_one()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
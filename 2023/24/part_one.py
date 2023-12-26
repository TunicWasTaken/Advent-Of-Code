import re
import numpy
import time
from itertools import combinations

time_start = time.time()


low = 200000000000000
high = 400000000000000


def parse():

    lines = open("input.txt").read().strip().split("\n")

    return [list(map(int, re.findall("-?\d+", line))) for line in lines]



def get_intersects():
    global low, high

    vectors = parse()
    res = 0

    for comb1, comb2 in combinations(vectors, 2):

        x1, y1, _, dx1, dy1, _ = comb1
        x2, y2, _, dx2, dy2, _ = comb2

        s1 = dy1 / dx1
        s2 = dy2 / dx2

        if s1 == s2:
            continue

        x, y = numpy.linalg.solve([[-s1, 1], [-s2, 1]], [y1 - s1 * x1, y2 - s2 * x2])

        if (x - x1) / dx1 < 0 or (x - x2) / dx2 < 0:
            continue

        if low <= x <= high and low <= y <= high:
            res += 1


    return res


result = get_intersects()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
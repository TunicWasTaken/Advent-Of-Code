import re
import time

time_start = time.time()


def simulate(bricks, floor):

    fallen = []
    while bricks:

        brick = bricks.pop(0)

        while not any(z == 1 for (_, _, z) in brick) and not any((x, y, z - 1) in floor for (x, y, z) in brick):

            brick = [(x, y, z - 1) for (x, y, z) in brick]


        fallen.append(brick)
        floor.update(brick)

    return fallen


def is_safe(bricks, b):

    i = bricks.index(b)
    floor = set([x for brick in bricks[:i] for x in brick if x not in b])
    aux = bricks[i + 1:]

    result = simulate(aux[:], floor)

    return result == aux


def sand_slabs():

    lines = open("input.txt").read().splitlines()

    bricks = []
    aux = []

    for line in lines:
        aux.append([int(x) for x in re.findall(r"\d+", line)])


    aux.sort(key= lambda brick: brick[2])
    for x1, y1, z1, x2, y2, z2 in aux:

        coords = []
        for i in range(x1, x2 + 1):
            coords.append((i, y1, z1))

        for j in range(y1, y2 + 1):
            coords.append((x1, j, z1))

        for p in range(z1, z2 + 1):
            coords.append((x1, y1, p))

        bricks.append(set(coords))

    safe = 0
    fallen = simulate(bricks, set())

    for brick in fallen:
        safe += is_safe(fallen, brick)


    return safe



result = sand_slabs()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
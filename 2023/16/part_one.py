from collections import defaultdict
import time

time_start = time.time()

GRID = open("input.txt").read().splitlines()
RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)


def energize(energized_dict, beam, direction):
    global GRID, RIGHT, LEFT, UP, DOWN

    while 0 <= beam[0] < len(GRID[0]) and 0 <= beam[1] < len(GRID) and direction not in energized_dict[beam]:
        energized_dict[beam].add(direction)

        # Changes the direction to the correct one after being reflected
        # If '/' then RIGHT -> UP, LEFT -> DOWN, UP -> RIGHT, DOWN -> LEFT
        # If '\' then RIGHT -> DOWN, LEFT -> UP, UP -> LEFT, DOWN -> RIGHT
        # If '-' or '|' and direction does not matche the orientation then
        # We recursively call energize to both new directions.
        match GRID[beam[1]][beam[0]]:
            case '/':
                direction = (-direction[1], -direction[0])
        
            case '\\':
                direction = (direction[1], direction[0])

            case '-' if direction in (UP, DOWN):
                energize(energized_dict, (beam[0] + 1, beam[1]), RIGHT)
                direction = LEFT

            case '|' if direction in (LEFT, RIGHT):
                energize(energized_dict, (beam[0], beam[1] + 1), DOWN)
                direction = UP

        
        beam = (beam[0] + direction[0], beam[1] + direction[1])

    return len(energized_dict)


result = energize(defaultdict(set), (0,0), RIGHT)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
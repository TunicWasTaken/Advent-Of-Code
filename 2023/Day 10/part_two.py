import time

time_start = time.time()


GRID = open("input.txt").read().strip().split("\n")

MOVES = {
    ("|", (1, 0)): (1, 0),
    ("|", (-1, 0)): (-1, 0),
    ("-", (0, 1)): (0, 1),
    ("-", (0, -1)): (0, -1),
    ("J", (0, 1)): (-1, 0),
    ("J", (1, 0)): (0, -1),
    ("L", (0, -1)): (-1, 0),
    ("L", (1, 0)): (0, 1),
    ("F", (0, -1)): (1, 0),
    ("F", (-1, 0)): (0, 1),
    ("7", (0, 1)): (1, 0),
    ("7", (-1, 0)): (0, -1)
}

START_COORD = next(
    (y_index, x_index) for y_index, row in enumerate(GRID) for x_index, row_value in enumerate(row) if row_value == "S"
)


def find_orientation():
    global GRID, START_COORD

    height, width = len(GRID), len(GRID[0])
    y, x = START_COORD

    directions = [(-1, 0, "|7F"), (1, 0, "|LJ"), (0, -1, "-FL"), (0, 1, "-J7")]

    for dir_y, dir_x, valid in directions:

        new_x = x + dir_x
        new_y = y + dir_y

        if 0 <= new_x < height and 0 <= new_y < width and GRID[new_y][new_x] in valid:
            if dir_y:
                return "|", (dir_y, dir_x)
            
            else:
                return "-", (dir_y, dir_x)
            


def find_path():
    global GRID, MOVES, START_COORD

    current_move, direction = find_orientation()
    y, x = START_COORD

    result = [(y, x)]

    while True:
        
        direction = MOVES[(current_move, direction)]
        dir_y, dir_x = direction

        x = x + dir_x
        y = y + dir_y

        if (y, x) == START_COORD:
            break

        current_move = GRID[y][x]
        result.append((y, x))

    return result
    
    
# Using the Shoelace Formula
def get_area(path):

    area = 0

    for i in range(len(path)):

        first_x, first_y = path[i]
        second_x, second_y = path[(i + 1) % len(path)]

        area += first_x * second_y - second_x * first_y

    return (abs(area) // 2)
            

result = get_area(find_path()) - (len(find_path()) // 2) + 1
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
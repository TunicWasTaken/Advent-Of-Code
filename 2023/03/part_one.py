from itertools import product
import time

time_start = time.time()

fdin = open("input.txt")

GRID = [list(line.strip()) for line in fdin]
HEIGHT = len(GRID)
WIDTH = len(GRID[0])
IS_PART_NUMBER = [[False for _ in range(WIDTH)] for __ in range(HEIGHT)]
digits = ['0','1','2','3','4','5','6','7','8','9']


def is_in_bounds(row, col):
    global HEIGHT, WIDTH

    return (0 <= row < HEIGHT) and (0 <= col < WIDTH)


def get_adjacent_positions(row, col):
    offset = [-1, 0, 1]
    adjacent_positions = []

    for row_offset, col_offset in product(offset, offset):
        if row_offset or col_offset:
            adj_row = row + row_offset
            adj_col = col + col_offset

            if is_in_bounds(adj_row, adj_col):
                adjacent_positions.append((adj_row,adj_col))
    
    return adjacent_positions


def mark_part_numbers(row, col):
    global GRID, IS_PART_NUMBER
    queue = [(row,col)]
    i = 0

    while i < len(queue):
        row, col = queue[i]

        if GRID[row][col] in digits:
            IS_PART_NUMBER[row][col] = True

        for adj_row, adj_col in get_adjacent_positions(row, col):
            if GRID[adj_row][adj_col] in digits and not IS_PART_NUMBER[adj_row][adj_col]:
                queue.append((adj_row,adj_col))
        
        i += 1


def extract_part_numbers():
    global GRID, IS_PART_NUMBER, HEIGHT, WIDTH

    numbers = []
    current_number = ""

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if IS_PART_NUMBER[row][col]:
                current_number += GRID[row][col]

            elif current_number:
                numbers.append(int(current_number))
                current_number = ""
        
        if current_number:
            numbers.append(int(current_number))
            current_number = ""
    
    return numbers


def gear_ratios_part_one():
    global GRID, HEIGH, WIDTH

    part_numbers = []

    for row in range(HEIGHT):
        for col in range(WIDTH):
            char = GRID[row][col]

            if char != "." and char not in digits:
                mark_part_numbers(row, col)

    part_numbers = extract_part_numbers()
    return sum(part_numbers)

result = gear_ratios_part_one()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
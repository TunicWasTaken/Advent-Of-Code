from collections import defaultdict
from itertools import product

fdin = open("input.txt")

GRID = [list(line.strip()) for line in fdin]
HEIGHT = len(GRID)
WIDTH = len(GRID[0])
GEAR_IDS = [[0 for _ in range(WIDTH)] for __ in range(HEIGHT)]
ID = 1
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
    global GRID, GEAR_IDS, ID
    queue = [(row,col)]
    i = 0

    while i < len(queue):
        row, col = queue[i]

        if GRID[row][col] in digits:
            GEAR_IDS[row][col] = ID

        for adj_row, adj_col in get_adjacent_positions(row, col):
            if GRID[adj_row][adj_col] in digits and not GEAR_IDS[adj_row][adj_col]:
                queue.append((adj_row,adj_col))
        
        i += 1


def extract_possible_gears():
    global GRID, GEAR_IDS, HEIGHT, WIDTH

    possible_gears = defaultdict(list)
    current_number = ""
    id = -1

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if GEAR_IDS[row][col]:
                id = GEAR_IDS[row][col]
                current_number += GRID[row][col]

            elif current_number:
                possible_gears[id].append(int(current_number))
                id = -1
                current_number = ""
        
        if current_number:
            possible_gears[id].append(int(current_number))
            id = -1
            current_number = ""
    
    return possible_gears


def extract_real_gears(possible_gears):
    gears = []

    for part_numbers in possible_gears.values():
        if len(part_numbers) == 2:
            gears.append(tuple(part_numbers))

    return gears

def gear_ratios_part_two():
    global GRID, HEIGHT, WIDTH, ID

    for row in range(HEIGHT):
        for col in range(WIDTH):
            char = GRID[row][col]

            if char == '*':
                mark_part_numbers(row, col)
                ID += 1

    possible_gears = extract_possible_gears()
    gears = extract_real_gears(possible_gears)

    gear_ratios = [gear[0] * gear[1] for gear in gears]
    return sum(gear_ratios)
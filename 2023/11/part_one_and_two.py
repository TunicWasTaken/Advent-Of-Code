import itertools
from copy import deepcopy
import time

time_start = time.time()


LINES = open("input.txt").read().splitlines()

def get_galaxies():
    global LINES
    
    galaxy_list = []

    for y_index, line in enumerate(LINES):
        for x_index, char in enumerate(line):
            if char == '#':
                galaxy_list.append([x_index, y_index])

    return galaxy_list
            


def expand_input(galaxy_list):
    global LINES

    # Create a new list that is a copy using the copy library
    # Since a normal attribution is just a pointer to the original list
    new_galaxy_list_part_one = deepcopy(galaxy_list)
    new_galaxy_list_part_two = deepcopy(galaxy_list)

    not_empty_rows = set([tup[1] for tup in galaxy_list])
    not_empty_columns = set([tup[0] for tup in galaxy_list])

    empty_rows = sorted(set(range(len(LINES))).difference(not_empty_rows))
    empty_columns = sorted(set(range(len(LINES))).difference(not_empty_columns))


    # Instead of adding one line we add 999999 lines
    # To make it so there's 1000000 lines between each non empty line.
    for galaxy_index, galaxy in enumerate(galaxy_list):
        for empty_row in empty_rows:
            if galaxy[1] > empty_row:
                new_galaxy_list_part_one[galaxy_index][1] += 1
                new_galaxy_list_part_two[galaxy_index][1] += 999999

        for empty_column in empty_columns:
            if galaxy[0] > empty_column:
                new_galaxy_list_part_one[galaxy_index][0] += 1
                new_galaxy_list_part_two[galaxy_index][0] += 999999

    
    return new_galaxy_list_part_one, new_galaxy_list_part_two



def get_distances(first_point, second_point):

    distance = 0

    # Zips the two tuples (a, b), (c, d) into (a, c), (b, d)
    # Then calculates the difference between each element of each tuple 
    # And adds its absolute value into the distance variable
    for first_point_coord, second_point_coord in zip(first_point, second_point):
        distance += abs(first_point_coord - second_point_coord)

    return distance



def cosmic_expansion():

    galaxy_list_part_one, galaxy_list_part_two = expand_input(get_galaxies())
    possible_combinations_part_one = list(itertools.combinations(galaxy_list_part_one, 2))
    possible_combinations_part_two = list(itertools.combinations(galaxy_list_part_two, 2))

    result_part_one = sum([get_distances(point[0], point[1]) for point in possible_combinations_part_one])
    result_part_two = sum([get_distances(point[0], point[1]) for point in possible_combinations_part_two])

    return result_part_one, result_part_two

    

part_one_result, part_two_result = cosmic_expansion()
time_end = time.time()
print(f"Part One Result: {part_one_result}, Part Two Result: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
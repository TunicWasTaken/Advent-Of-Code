import re
import math
import time

time_start = time.time()

LINES = open("input.txt").read().splitlines()
DIRECTIONS = LINES[0]


def haunted_wasteland():
    global LINES, DIRECTIONS

    network_map = {}
    current_location_part_one = "AAA"
    current_locations_part_two = []
    steps_to_reach_part_one = 0
    steps_to_reach_part_two = []

    for index in range(2,len(LINES)):

        origin , destinations = LINES[index].split(' = ')
        destinations = re.sub(r"[()]", "", destinations)
        left_destination, right_destination = destinations.split(', ')
        
        if origin not in network_map:
            network_map[origin] = (left_destination, right_destination)

        if origin.endswith('A'):
            current_locations_part_two.append(origin)


    index = 0
    while(index < len(DIRECTIONS)):

        if current_location_part_one == "ZZZ":
            break
        
        if DIRECTIONS[index] == 'L':
            current_location_part_one = network_map[current_location_part_one][0]
            steps_to_reach_part_one += 1

        else:
            current_location_part_one = network_map[current_location_part_one][1]
            steps_to_reach_part_one += 1

        
        if index == len(DIRECTIONS) - 1:
            index = 0

        else:
            index += 1


    for current_location in current_locations_part_two:

        steps = 0
        index = 0

        while(index < len(DIRECTIONS)):

            if current_location.endswith('Z'):
                steps_to_reach_part_two.append(steps)
                break
            
            if DIRECTIONS[index] == 'L':
                current_location = network_map[current_location][0]
                steps += 1

            else:
                current_location = network_map[current_location][1]
                steps += 1

            
            if index == len(DIRECTIONS) - 1:
                index = 0

            else:
                index += 1

    
    return steps_to_reach_part_one, math.lcm(*steps_to_reach_part_two)
        

part_one_result, part_two_result = haunted_wasteland()
time_end = time.time()
print(f"Part One Result: {part_one_result}, Part Two Result: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
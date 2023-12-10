import re
import math
import time

time_start = time.time()

LINES = open("input.txt").read().splitlines()
DIRECTIONS = LINES[0]


def haunted_wasteland():
    global LINES, DIRECTIONS

    network_map = {}
    current_locations = []
    steps_to_reach = []

    for index in range(2,len(LINES)):

        origin , destinations = LINES[index].split(' = ')
        destinations = re.sub(r"[()]", "", destinations)
        left_destination, right_destination = destinations.split(', ')
        
        if origin not in network_map:
            network_map[origin] = (left_destination, right_destination)

        if origin.endswith('A'):
            current_locations.append(origin)


    for current_location in current_locations:

        steps = 0
        index = 0

        while(index < len(DIRECTIONS)):

            if current_location.endswith('Z'):
                steps_to_reach.append(steps)
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

    
    return math.lcm(*steps_to_reach)
        

result = haunted_wasteland()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
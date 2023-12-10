import re
import time

time_start = time.time()

LINES = open("input.txt").read().splitlines()
DIRECTIONS = LINES[0]


def haunted_wasteland():
    global LINES, DIRECTIONS

    network_map = {}
    current_location = "AAA"
    steps_to_reach = 0

    for index in range(2,len(LINES)):

        origin , destinations = LINES[index].split(' = ')
        destinations = re.sub(r"[()]", "", destinations)
        left_destination, right_destination = destinations.split(', ')
        
        if origin not in network_map:
            network_map[origin] = (left_destination, right_destination)

    index = 0
    while(index < len(DIRECTIONS)):

        if current_location == "ZZZ":
            return steps_to_reach
        
        if DIRECTIONS[index] == 'L':
            current_location = network_map[current_location][0]
            steps_to_reach += 1

        else:
            current_location = network_map[current_location][1]
            steps_to_reach += 1

        
        if index == len(DIRECTIONS) - 1:
            index = 0

        else:
            index += 1
            
        

result = haunted_wasteland()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
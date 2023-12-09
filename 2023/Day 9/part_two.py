from itertools import pairwise
import time

time_start = time.time()

LINES = open("input.txt").read().splitlines()


def mirage_maintenance():
    global LINES

    sequences = [[int(n) for n in line.split()] for line in LINES]
    extrapolated_values = []

    for current_sequence in sequences:

        current_sequence = current_sequence[::-1]
        extrapolated_value = current_sequence[-1]
        
        while not all(number == 0 for number in current_sequence):

            current_sequence = [y - x for x,y in pairwise(current_sequence)]
            extrapolated_value += current_sequence[-1]

        extrapolated_values.append(extrapolated_value)
    
    return sum(extrapolated_values)

        
result = mirage_maintenance()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
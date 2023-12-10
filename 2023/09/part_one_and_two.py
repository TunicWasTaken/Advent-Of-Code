from itertools import pairwise
import time

time_start = time.time()

LINES = open("input.txt").read().splitlines()


def mirage_maintenance(current_sequence):

    extrapolated_value = current_sequence[-1]
        
    while not all(number == 0 for number in current_sequence):

        current_sequence = [y - x for x,y in pairwise(current_sequence)]
        extrapolated_value += current_sequence[-1]

    
    return extrapolated_value


sequences = [[int(n) for n in line.split()] for line in LINES]
part_one_result = sum(mirage_maintenance(sequence) for sequence in sequences)
part_two_result = sum(mirage_maintenance(sequence[::-1]) for sequence in sequences)
time_end = time.time()
print(f"Part One Result: {part_one_result}, Part Two Result: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
import re
import math
import time

time_start = time.time()

FDIN = open("input.txt")

LINES = FDIN.read().splitlines()
TIMES = list(map(int, re.findall(r"[0-9]+",(LINES[0].split(":")[1]))))
DISTANCES = list(map(int, re.findall(r"[0-9]+",(LINES[1].split(":")[1]))))
TIME = int(re.sub(r" ", "", (LINES[0].split(":")[1])))
DISTANCE = int(re.sub(r" ", "", (LINES[1].split(":")[1])))


# Inequality => (TIME * x) - DISTANCE - x^2 > 0
# a = -1, b = TIME, c = - DISTANCE
def wait_for_it_part_one():
    global TIMES, DISTANCES

    winning_times = []

    for index, time in enumerate(TIMES):

        quadratic_result_plus = (- time + math.sqrt(time**2 - 4*DISTANCES[index])) / -2
        quadratic_result_minus = (- time - math.sqrt(time**2 - 4*DISTANCES[index])) / -2

        quadratic_result_plus = math.ceil(quadratic_result_plus)
        quadratic_result_minus = math.floor(quadratic_result_minus)

        winning_times.append(quadratic_result_minus - quadratic_result_plus + 1)

    return math.prod(winning_times)



# Brute force way to calculate the result for Part One.
def wait_for_it_brute_force_part_one():
    global LINES, TIMES, DISTANCES

    winning_ranges = []
    total = 1

    for index, time in enumerate(TIMES):

        current_time = 0

        for i in range(0, time + 1):

            current_time = time - i
            total_distace = current_time * i

            if total_distace > DISTANCES[index]:
                
                winning_ranges.append((i, time - i))
                break

    
    for winning_range in winning_ranges:
        total *= (winning_range[1] - winning_range[0] + 1)

    return total


# Inequality => (TIME * x) - DISTANCE - x^2 > 0
# a = -1, b = TIME, c = - DISTANCE
def wait_for_it_part_two():
    global TIME, DISTANCE

    quadratic_result_plus = (- TIME + math.sqrt(TIME**2 - 4*DISTANCE)) / -2
    quadratic_result_minus = (- TIME - math.sqrt(TIME**2 - 4*DISTANCE)) / -2

    quadratic_result_plus = math.ceil(quadratic_result_plus)
    quadratic_result_minus = math.floor(quadratic_result_minus)

    return (quadratic_result_minus - quadratic_result_plus + 1)



# Brute force way to calculate the result for Part Two.
def wait_for_it_brute_force_part_two():
    global LINES, TIME, DISTANCE

    for i in range(0, TIME + 1):

        current_time = TIME - i
        total_distance = current_time * i

        if total_distance > DISTANCE:
            return ((TIME - i) - i + 1)



part_one_result = wait_for_it_part_one()
part_two_result = wait_for_it_part_two()
time_end = time.time()
print(f"Result Part One: {part_one_result}, Result Part Two: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
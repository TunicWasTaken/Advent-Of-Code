import re
import math
import time

time_start = time.time()

FDIN = open("input.txt")

LINES = FDIN.read().splitlines()
TIMES = list(map(int, re.findall(r"[0-9]+",(LINES[0].split(":")[1]))))
DISTANCES = list(map(int, re.findall(r"[0-9]+",(LINES[1].split(":")[1]))))


# Inequality => (TIME * x) - DISTANCE - x^2 > 0
# a = -1, b = TIME, c = - DISTANCE
def wait_for_it():
    global TIMES, DISTANCES

    winning_times = []

    for index, time in enumerate(TIMES):

        quadratic_result_plus = (- time + math.sqrt(time**2 - 4*DISTANCES[index])) / -2
        quadratic_result_minus = (- time - math.sqrt(time**2 - 4*DISTANCES[index])) / -2

        quadratic_result_plus = math.ceil(quadratic_result_plus)
        quadratic_result_minus = math.floor(quadratic_result_minus)

        winning_times.append(quadratic_result_minus - quadratic_result_plus + 1)

    return math.prod(winning_times)



# Brute force way to calculate the result.
def wait_for_it_brute_force():
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


result = wait_for_it()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
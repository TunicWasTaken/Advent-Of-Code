import re
import math
import time

time_start = time.time()

FDIN = open("input.txt")

LINES = FDIN.read().splitlines()
TIME = int(re.sub(r" ", "", (LINES[0].split(":")[1])))
DISTANCE = int(re.sub(r" ", "", (LINES[1].split(":")[1])))


# Inequality => (TIME * x) - DISTANCE - x^2 > 0
# a = -1, b = TIME, c = - DISTANCE
def wait_for_it():
    global TIME, DISTANCE

    quadratic_result_plus = (- TIME + math.sqrt(TIME**2 - 4*DISTANCE)) / -2
    quadratic_result_minus = (- TIME - math.sqrt(TIME**2 - 4*DISTANCE)) / -2

    quadratic_result_plus = math.ceil(quadratic_result_plus)
    quadratic_result_minus = math.floor(quadratic_result_minus)

    return (quadratic_result_minus - quadratic_result_plus + 1)



# Brute force way to calculate the result.
def wait_for_it_brute_force():
    global LINES, TIME, DISTANCE

    for i in range(0, TIME + 1):

        current_time = TIME - i
        total_distance = current_time * i

        if total_distance > DISTANCE:
            return ((TIME - i) - i + 1)



result = wait_for_it()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
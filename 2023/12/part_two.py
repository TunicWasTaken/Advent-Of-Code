from itertools import product
import functools
import time

time_start = time.time()


LINES = open("input.txt").read().splitlines()
BINTOCHAR = {0: '.', 1: '#'}


def get_springs():
    global LINES

    springs = []

    for line in LINES:

        line = line.split(' ')
        line[0] = "?".join([line[0]] * 5)
        line[1] = tuple(int(num) for num in line[1].split(','))
        line[1] = line[1] * 5

        springs.append(line)
       

    return springs
    
@functools.cache
def get_n_arrangements(spring, counts_left, current_count_len):

    if len(spring) == 0:
        if len(counts_left) == 0 and current_count_len == 0:
            return 1
        
        elif len(counts_left) == 1 and current_count_len == counts_left[0]:
            return 1
        
        else:
            return 0
        

    if len(counts_left) > 0 and current_count_len > counts_left[0]:
        return 0
    
    elif len(counts_left) == 0 and current_count_len > 0:
        return 0
    


    number_of_arrangements = 0
    spring_char = spring[0]

    if spring_char == '#' or spring_char == '?':
        number_of_arrangements += get_n_arrangements(spring[1:], counts_left, current_count_len + 1)

    if spring_char == '.' or spring_char == '?':
        
        if len(counts_left) > 0 and current_count_len == counts_left[0]:
            number_of_arrangements += get_n_arrangements(spring[1:], counts_left[1:], 0)

        elif current_count_len == 0:
            number_of_arrangements += get_n_arrangements(spring[1:], counts_left, 0)

    
    return number_of_arrangements



def hot_springs():

    possible_arrangements = []
    springs = get_springs()

    for current_spring, counts in springs:

        number_of_arrangements = get_n_arrangements(current_spring, counts, 0)
        possible_arrangements.append(number_of_arrangements)

    return sum(possible_arrangements)


result = hot_springs()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
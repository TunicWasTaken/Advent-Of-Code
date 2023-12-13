import functools
import time

time_start = time.time()

LINES = open("input.txt").read().splitlines()


def get_springs():
    global LINES

    springs_part_one = []
    springs_part_two = []

    for line in LINES:

        line_part_one = line.split(' ')
        line_part_one[1] = tuple(int(num) for num in line_part_one[1].split(','))

        line_part_two = line.split(' ')
        line_part_two[0] = "?".join([line_part_two[0]] * 5)
        line_part_two[1] = tuple(int(num) for num in line_part_two[1].split(','))
        line_part_two[1] = line_part_two[1] * 5

        springs_part_one.append(line_part_one)
        springs_part_two.append(line_part_two)
       

    return springs_part_one, springs_part_two
    

@functools.cache
def get_number_of_arrangements(spring, counts_left, current_count_len):

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
        number_of_arrangements += get_number_of_arrangements(spring[1:], counts_left, current_count_len + 1)

    if spring_char == '.' or spring_char == '?':
        if len(counts_left) > 0 and current_count_len == counts_left[0]:
            number_of_arrangements += get_number_of_arrangements(spring[1:], counts_left[1:], 0)

        elif current_count_len == 0:
            number_of_arrangements += get_number_of_arrangements(spring[1:], counts_left, 0)

    
    return number_of_arrangements


def hot_springs():

    possible_arrangements_part_one = []
    possible_arrangements_part_two = []
    springs_part_one, springs_part_two = get_springs()

    for current_spring, counts in springs_part_one:

        number_of_arrangements = get_number_of_arrangements(current_spring, counts, 0)
        possible_arrangements_part_one.append(number_of_arrangements)

    for current_spring, counts in springs_part_two:

        number_of_arrangements = get_number_of_arrangements(current_spring, counts, 0)
        possible_arrangements_part_two.append(number_of_arrangements)

    return sum(possible_arrangements_part_one), sum(possible_arrangements_part_two)


part_one_result, part_two_result = hot_springs()
cache_info_hits = get_number_of_arrangements.cache_info().hits
cache_info_misses = get_number_of_arrangements.cache_info().misses
cache_info_size = get_number_of_arrangements.cache_info().currsize
time_end = time.time()
print(f"Part One Result: {part_one_result}, Part Two Result: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms with {cache_info_hits} Hits, {cache_info_misses} Misses and with a Size of {cache_info_size}")
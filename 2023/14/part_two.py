import time

time_start = time.time()


def rotate_matrix(platform, direction):
    if direction:
        platform = platform[::-1]
        return [[line[i] for line in platform] for i in range(len(platform[0]))]
    
    return [[line[i] for line in platform] for i in range(len(platform[0]))][::-1]


def tilt(platform):

    for row in platform:

        empty_position = 0

        for x, char in enumerate(row):
            if char == "O":
                row[x] = "."
                row[empty_position] = "O"
                empty_position += 1
            
            elif char == "#":
                empty_position = x + 1
    

    return platform


def cycle(platform):

    for i in range(4):
        platform = tilt(platform)
        platform = rotate_matrix(platform, True)

    return platform




def parabolic_dish():

    lines = open("input.txt").read().splitlines()

    platform = [list(line) for line in lines]
    platform = rotate_matrix(platform, False)
    
    cycles = {}
    number_of_cycles = 0

    while True:
        platform_string = "".join(["".join(line) for line in platform])
        if platform_string in cycles:
            break


        cycles[platform_string] = number_of_cycles
        platform = cycle(platform)
        number_of_cycles += 1

    

    last_cycle = number_of_cycles - cycles[platform_string]
    last_cycle_position = (1000000000 - number_of_cycles) % last_cycle
    end_index = number_of_cycles - last_cycle + last_cycle_position

    for platform_string, index in cycles.items():
        if index == end_index:
            break


    height = len(platform)
    width = len(platform[0])
    platform = []

    for i in range(height):
        platform.append(list(platform_string[height * i : height * i + width]))


    total_weight = 0
    width = len(platform[0])

    for row in platform:
        for x, char in enumerate(row):
            if char == "O":
                total_weight += width - x
    
    return total_weight


result = parabolic_dish()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
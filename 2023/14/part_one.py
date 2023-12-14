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



def parabolic_dish():

    lines = open("input.txt").read().splitlines()

    platform = [list(line) for line in lines]
    platform = rotate_matrix(platform, False)
    platform = tilt(platform)
    
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
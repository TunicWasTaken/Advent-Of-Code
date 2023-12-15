import time

time_start = time.time()



def helper_hash(string):

    value = 0

    for char in string:

        value = (((value + ord(char)) * 17) % 256)

    return value


def lens_library():

    sequences = open("input.txt").read().split(",")
    sequences = [helper_hash(sequence) for sequence in sequences]

    return sum(sequences)


result = lens_library()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
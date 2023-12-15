import time
import re

time_start = time.time()


def helper_hash(string):

    box_id = 0

    for char in re.search(r"[a-zA-Z]+", string).group(0):
        box_id = (((box_id + ord(char)) * 17) % 256)


    return box_id
    


def lens_library():

    sequences = open("input.txt").read().split(",")
    hashmap = {}

    for sequence in sequences:
        
        is_dash = sequence[-1] == '-'
        box_id = helper_hash(sequence)

        if is_dash:
            sequence_label = sequence[:-1]

        else:
            sequence_label = sequence[:-2]
            lens = int(sequence[-1])


        box_index = next((index for index, (label, lens) in enumerate(hashmap.get(box_id, [])) if label == sequence_label), -1)

        if not is_dash:
            if box_index == -1:
                if box_id not in hashmap:
                    hashmap[box_id] = []

                hashmap[box_id].append([sequence_label, lens])

            else:
                hashmap[box_id][box_index][1] = lens

        else:
            if box_index > -1:
                hashmap[box_id].remove(hashmap[box_id][box_index])

    

    return sum((1 + box) * (box_index + 1) * lens[1] for box in hashmap for box_index, lens in enumerate(hashmap[box]))



result = lens_library()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
import re
import time

time_start = time.time()

FDIN = open("input.txt")
LINES = FDIN.read().split("\n\n")
SEEDS = list(map(int, re.findall(r"\d+", LINES[0].split(":")[1])))


def create_mappings():
    global LINES

    mappings = []

    for first_index, current_mapping in enumerate(LINES[1:]):
        mappings.append([])

        empty_space, *current_mapping = current_mapping.split("\n")
        current_maps = list((int(src), int(dest), int(delta)) for dest, src, delta in map(str.split, current_mapping))
        
        for (min_src, min_dest, delta) in current_maps:
            mappings[first_index].append(((min_src, min_src + delta), (min_dest, min_dest + delta)))

    return mappings
        

def get_location(seed, mappings):

    location = seed

    for current_map in mappings:
        for (src_min, src_max), (dest_min, dest_max) in current_map:
            if src_min <= location <= src_max:
                location = location + (dest_min - src_min)
                break

    return location
        


def almanac():
    global SEEDS

    locations = []
    mappings = create_mappings()

    for seed in SEEDS:
        locations.append(get_location(seed, mappings))

    return min(locations)



index = 1
for line in LINES[1:]:
    LINES[index] = LINES[index].split(":")[1]
    index += 1
    

result = almanac()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
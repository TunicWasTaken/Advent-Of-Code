import re
import time

time_start = time.time()

FDIN = open("input.txt")
LINES = FDIN.read().split("\n\n")
SEEDS = list(map(int, re.findall(r"\d+", LINES[0].split(":")[1])))
SEEDS = [(SEEDS[i], SEEDS[i] + SEEDS[i+1]) for i in range(0, len(SEEDS), 2)]


def create_mappings():
    global LINES

    mappings = []

    for index, current_mapping in enumerate(LINES[1:]):
        mappings.append([])

        empty_char, *current_mapping = current_mapping.split("\n")
        current_maps = list((int(src), int(dest), int(delta)) for dest, src, delta in map(str.split, current_mapping))
        
        for (src_start, dest_start, delta) in current_maps:
            mappings[index].append(((src_start, src_start + delta - 1), (dest_start, dest_start + delta - 1)))

    return mappings

        
def get_location(seed, mappings):

    location = seed

    for current_map in mappings:
        for (src_start, src_end), (dest_start, dest_end) in current_map:
            if src_start <= location <= src_end:
                location = location + (dest_start - src_start)
                break

    return location
        

def get_intersection(seed_range, map_range):
    
    if map_range[0] < seed_range[0]:
        intersect_min = map_range
    else:
        intersect_min = seed_range

    if map_range[0] < seed_range[0]:
        intersect_max = seed_range
    else:
        intersect_max = map_range

    if intersect_min[1] < intersect_max[0]:
        return False
    else:
        if intersect_min[1] < intersect_max[1]:
            return (intersect_max[0], intersect_min[1])
        else:
            return (intersect_max[0], intersect_max[1])
        


def get_values(ranges, mapping):

    current_ranges = ranges
    new_ranges = []

    for (src_start, src_end), (dest_start, dest_end) in mapping:

        iter_ranges = current_ranges

        for (seed_start, seed_end) in iter_ranges:

            intersect = get_intersection((src_start, src_end), (seed_start, seed_end))

            if intersect:
                new_ranges.append(sorted((dest_start + (intersect[0] - src_start), dest_start + (intersect[1] - src_start))))

                current_ranges = [current_range for current_range in current_ranges if current_range[0] != seed_start or current_range[1] != seed_end]


                if intersect[0] - seed_start > 0:
                    current_ranges.append([seed_start, intersect[0] - 1])

                
                if seed_end - intersect[1] > 0:
                    current_ranges.append([intersect[1] + 1, seed_end])

    return new_ranges + current_ranges

            
def almanac():
    global SEEDS

    mappings = create_mappings()
    seed_ranges = SEEDS

    for mapping in mappings:

        seed_ranges = get_values(seed_ranges, mapping)

    return min(min(seed_ranges))



# Brute Force Method. Don't know if it works because it would take way too long. So I spent even more time making a more efficient solution.
# Requires changing of almanac to Part One's version.
def almanac_brute_force():
    global SEEDS

    locations = []

    for (seed_start, delta) in SEEDS:

        new_seeds = list(range(seed_start, seed_start + delta - 1))
        locations.append(almanac(new_seeds))

    return min(locations)



index = 1
for line in LINES[1:]:
    LINES[index] = LINES[index].split(":")[1]
    index += 1
    

seed_ranges = SEEDS
result = almanac()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
import time
time_start = time.time()

def is_safe(levels):
    direction = set()
    for i in range(len(levels)-1):
        diff = levels[i] - levels[i+1]

        if diff > 0:
            direction.add(-1) # Decreasing
        elif diff < 0:
            direction.add(1) # Increasing
        else:
            return False # Equal

        if abs(diff) > 3 or len(direction) > 1:
            return False
        
    return True

def part_two():
    data = open("input.txt")
    res = 0

    for line in data:
        levels = [int(v) for v in line.replace("\n", '').split(" ")]

        if is_safe(levels):
            res += 1
        else:
            for i in range(len(levels)):
                levels_cpy = levels.copy()
                levels_cpy.pop(i)
                if is_safe(levels_cpy):
                    res += 1
                    break
        

    return res
        
res = part_two()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
import time
import re
time_start = time.time()

def part_two():
    data = open("input.txt")
    res = 0
    enabled = True

    for line in data:
        instructions = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)", line)

        for instruction in instructions:
            if "do()" in instruction:
                enabled = True
            elif "don't()" in instruction:
                enabled = False
            elif enabled:
                n1,n2 = re.findall(r"[0-9]+", instruction)
                res += int(n1)*int(n2)
        
    return res
        
res = part_two()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
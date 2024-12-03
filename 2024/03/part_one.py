import time
import re
time_start = time.time()

def part_one():
    data = open("input.txt")
    res = 0
    
    for line in data:
        mul_list = re.findall(r"mul\([0-9]+,[0-9]+\)", line)

        for mul in mul_list:
            n1,n2 = re.findall(r"[0-9]+", mul)
            res += int(n1)*int(n2)
        
    return res
        
res = part_one()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
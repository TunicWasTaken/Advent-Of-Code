import time
time_start = time.time()

def part_two():
    data = open("input.txt")
    res, larr, rcounter = 0, [], {}

    for line in data:
        l,r = line.replace('\n','').split('   ')
        larr.append(int(l))
        r = int(r)
        
        if r not in rcounter:
            rcounter[r] = 1
        else:
            rcounter[r] += 1

    for num in larr:
        if num not in rcounter:
            continue

        res += num * rcounter[num]

    return res
        
res = part_two()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
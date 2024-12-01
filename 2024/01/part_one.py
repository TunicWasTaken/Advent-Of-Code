import time
time_start = time.time()

def part_one():
    data = open("input.txt")
    res, larr, rarr = 0, [], []

    for line in data:
        l,r = line.replace('\n','').split('   ')
        larr.append(int(l))
        rarr.append(int(r))

    larr.sort()
    rarr.sort()

    for ind in range(len(larr)):
        res += abs(larr[ind] - rarr[ind])

    return res
        
res = part_one()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
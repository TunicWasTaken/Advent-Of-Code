import time
import re
time_start = time.time()

def get_diagonal(data):
    shift = [line[i:] for i, line in enumerate(data)]
    diagonal = " ".join("".join(line) for line in zip(*shift))

    return diagonal


def part_one():
    data = open("input.txt").read().splitlines()
    
    horizontal = " ".join(data)
    vertical = " ".join("".join(column) for column in zip(*data))
    
    pad = "." * (len(data[0]) - 1)
    padded_line = [pad + line + pad for line in data]
    diagonal = get_diagonal(padded_line)
    anti_diagonal = get_diagonal(padded_line[::-1])

    transformed_data = " ".join((horizontal,vertical,diagonal,anti_diagonal))
    return len(re.findall(r"(?=(XMAS|SAMX))", transformed_data))

        
res = part_one()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
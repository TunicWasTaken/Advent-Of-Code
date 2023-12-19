import re
import functools
import time

time_start = time.time()


OPERATORS = {'>': lambda x, y: x > y, '<': lambda x, y: x < y}

def parse_input():

    wfs, _ = [line.split("\n") for line in open("input.txt").read().split("\n\n")]
    
    workflows = {}
    for workflow in wfs:

        name, _, end_dest = re.findall(r"(\w+){(.*),(\w+)}", workflow)[0]
        
        workflow_rules = [(part_type, op, int(val), dest) for part_type, op, val, dest in re.findall(r"(\w)(<|>)(\d+):(\w+)", workflow)]
        workflows[name] = (workflow_rules, end_dest)


    return workflows


TOTAL_SUM = 0
def check_ranges(ranges, workflow, workflows):
    global TOTAL_SUM

    leftover_ranges = {key:[x for x in range] for (key, range) in ranges.items()}
    
    for part_type, op, val, dest in workflow[0]:
        ranges_copy = {key:[x for x in range] for (key, range) in leftover_ranges.items()}

        if op == '<':
            ranges_copy[part_type][1] = val - 1
            leftover_ranges[part_type][0] = val

        else:
            ranges_copy[part_type][0] = val + 1
            leftover_ranges[part_type][1] = val

        if dest == 'A':
            product = functools.reduce(lambda x, y: x * y, [range[1] - range[0] + 1 for range in ranges_copy.values()], 1)
            TOTAL_SUM += product

        elif dest == 'R':
            pass

        else:
            check_ranges(ranges_copy, workflows[dest], workflows)

    
    if workflow[1] == 'A':
        product = functools.reduce(lambda x, y: x * y, [range[1] - range[0] + 1 for range in leftover_ranges.values()], 1)
        TOTAL_SUM += product

    elif workflow[1] == 'R':
        pass

    else:
        check_ranges(leftover_ranges, workflows[workflow[1]], workflows)


        
def aplenty():

    workflows = parse_input()
    start_ranges = {part_type:range for part_type,range in zip(list('xmas'), [[1, 4000]] * 4)}

    check_ranges(start_ranges, workflows['in'], workflows)
    

aplenty()
result = TOTAL_SUM
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
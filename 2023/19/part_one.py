import re
import time

time_start = time.time()


OPERATORS = {'>': lambda x, y: x > y, '<': lambda x, y: x < y}

def parse_input():

    wfs, rtgs = [line.split("\n") for line in open("input.txt").read().split("\n\n")]

    ratings = []

    for rating in rtgs:
        ratings.append({part_type:int(part) for (part_type, part) in [[part_types for part_types in part_rating.split("=")] for part_rating in rating[1:-1].split(",")]})

    
    workflows = {}
    for workflow in wfs:

        name, _, end_dest = re.findall(r"(\w+){(.*),(\w+)}", workflow)[0]
        
        workflow_rules = [(part_type, op, int(val), dest) for part_type, op, val, dest in re.findall(r"(\w)(<|>)(\d+):(\w+)", workflow)]
        workflows[name] = (workflow_rules, end_dest)


    return workflows, ratings


def process_workflow(rating, workflow, workflows):

        for part_type, op, val, dest in workflow[0]:
            if OPERATORS[op](rating[part_type], val):
                if dest == 'A':
                    return True
                
                elif dest == 'R':
                    return False
                
                else:
                    return process_workflow(rating, workflows[dest], workflows)
                
        if workflow[1] == 'A':
            return True
        
        elif workflow[1] == 'R':
            return False
        
        else:
            return process_workflow(rating, workflows[workflow[1]], workflows)
             



def aplenty():

    workflows, ratings = parse_input()

    return sum([sum(rating.values()) for rating in ratings if process_workflow(rating, workflows['in'], workflows)])

    

result = aplenty()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
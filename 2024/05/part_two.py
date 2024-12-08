import time
time_start = time.time()

def parse(page_rules, orders):

    rules: dict[int, set[int]] = {}
    for rule in page_rules.split("\n"):
        a,b = rule.split("|")
        if int(a) in rules:
            rules[int(a)].add(int(b))
        else:
            rules[int(a)] = {int(b)}

    return rules, [[int(a) for a in order.split(",")] for order in orders.split("\n")]


def is_valid(rules, orders):

    check = set()
    for order in orders:
        if check & rules.get(order, set()):
            return False
        check.add(order)

    return True


def fix(rules, order, mid):

    candidate = order.pop()
    if not order:
        return candidate
    
    gt_cand = order - rules.get(candidate, set())
    lt_cand = order - gt_cand

    N = len(lt_cand)
    if N == mid:
        return candidate
    
    if mid < N:
        return fix(rules, lt_cand, mid)

    return fix(rules, gt_cand, mid - N - 1)



def part_two():
    page_rules, orders = open("input.txt").read().split("\n\n")
    res = 0

    rules, orders = parse(page_rules, orders)
    for order in orders:
        mid = len(order) // 2
        if not is_valid(rules, order):
            res += fix(rules, set(order), mid)


    return res


res = part_two()
time_end = time.time()
print(f"Result: {res}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
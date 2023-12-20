from collections import deque
import time

time_start = time.time()

# For the code to work on the second example input
# It's required to change everything referencing "rx" to output
def parse_input():

    lines = open("input.txt").read().splitlines()

    adjacents = {}
    conjunctions = {}
    flipflops = {}
    rx_conjunction = ""
    for line in lines:

        module, dests = line.split(" -> ")
        dests = dests.split(', ')
        module_type = module[0]

        if module == 'broadcaster':
            adjacents[module] = dests

        else:
            label = module[1:]
            adjacents[label] = dests

        if "rx" in dests:
            rx_conjunction = label

        if module_type == '&':
            conjunctions[label] = {}

        if module_type == '%':
            flipflops[label] = 0

    for label, dests in adjacents.items():
        for dest in dests:
            if dest in conjunctions:
                conjunctions[dest][label] = 0

    return adjacents, conjunctions, flipflops, rx_conjunction


def press():
    global total_low_pulses, total_high_pulses, presses

    presses += 1
    total_low_pulses += 1 + len(adjacents["broadcaster"])
    queue = deque()

    for dest in adjacents["broadcaster"]:
        queue.append((0, "broadcaster", dest))

    while queue:

        pulse_type, src, label = queue.popleft()
        to_send = 0

        if label == "rx":
            continue

        if label in conjuctions:
            conjuctions[label][src] = pulse_type

            if any(val == 0 for val in conjuctions[label].values()):
                to_send = 1

        if label in flipflops:
            if pulse_type:
                continue

            flipflops[label] = not flipflops[label]
            if flipflops[label]:
                to_send = 1


        if to_send:
            total_high_pulses += len(adjacents[label])
        else:
            total_low_pulses += len(adjacents[label])


        for dest in adjacents[label]:
            queue.append((to_send, label, dest))


        for label, val in conjuctions[rx_conjuction].items():
            if val and label not in rx_conjuction_presses:
                rx_conjuction_presses[label] = presses
        



adjacents, conjuctions, flipflops, rx_conjuction = parse_input()
total_low_pulses = 0
total_high_pulses = 0
presses = 0
rx_conjuction_presses = {}

for _ in range(1000):
    press()

result = total_low_pulses * total_high_pulses
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
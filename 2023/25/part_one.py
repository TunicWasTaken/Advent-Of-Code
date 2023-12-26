import networkx as nx
import time

time_start = time.time()

def snoverload():

    graph = nx.Graph()

    for line in open("input.txt").read().splitlines():

        row = line.strip().split(':')

        for target in row[1].strip().split():
            graph.add_edge(row[0].strip(), target)


    costs = []
    for edge in graph.edges:

        graph.remove_edge(*edge)
        costs.append((edge, nx.shortest_path_length(graph, *edge)))
        graph.add_edge(*edge)

    costs = sorted(costs, key = lambda x: x[1], reverse = True)
    [graph.remove_edge(*costs[i][0]) for i in range(3)]

    return len(nx.node_connected_component(graph, costs[0][0][0])) * len(nx.node_connected_component(graph, costs[0][0][1]))



result = snoverload()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")
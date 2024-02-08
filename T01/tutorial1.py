graph = {
    'S': {('A', 1), ('B', 5),  ('C', 15)},
    'A': {('G', 10), ('S', 1)},
    'B': {('G', 5), ('S', 5)},
    'C': {('G', 5), ('S', 15)},
    'G': set()
}

from time import sleep
from priority_queue import PriorityQueue
from collections import defaultdict

# Return the path found
def uniform_cost_search(graph, initial_node, goal_test, is_tree, is_update):
    print("nodes expanded: ", end="")
    frontier = PriorityQueue(order='min')
    visited = set()

    initial_node = (initial_node, "S")
    frontier.append(initial_node, 0)
    visited.add(initial_node)

    while frontier:
        acc_cost, cur_node = frontier.pop()
        print(cur_node[0], end="")

        if goal_test(cur_node[0]):
            print()
            return cur_node[1]

        visited.add(cur_node[0])

        for next_node, edge_cost in graph[cur_node[0]]:
            if not is_tree and next_node in visited:
                continue

            frontier.append((next_node, cur_node[1] + next_node), acc_cost + edge_cost)

    return False


print("=====")
print("Tree")
print("=====")
p = uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=True, is_update=False)
print("path: " + p)
assert(p=="SBG")

print("=====")
print("Graph")
print("=====")
p = uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=False, is_update=True)
print("path: " + p)
assert(p=="SBG")

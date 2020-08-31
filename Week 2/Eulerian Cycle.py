# python3
import numpy as np


class Node:
    def __init__(self, key=-1):
        self.in_degree = 0
        self.out_degree = 0
        self.key = key
        self.children = []


def find_eulerian_cycle(graph):
    current_node = graph[0]
    circuit = []
    path = [current_node.key]

    while len(path):
        current_node = graph[path[-1] - 1]
        if len(current_node.children) == 0:
            current_node = graph[path.pop() - 1]
            circuit.append(current_node.key)
            continue
        path.append(current_node.children[0].key)
        current_node.children.pop(0)
    circuit.reverse()
    return circuit[:-1]


def build_graph(n, m, edges):
    graph = []
    for i in range(n):
        graph.append(Node(i + 1))

    for edge in edges:
        src = edge[0] - 1
        dst = edge[1] - 1
        graph[src].children.append(graph[dst])
        graph[src].out_degree += 1
        graph[dst].in_degree += 1
    return graph


def is_path_available(graph):
    first_flag = False
    second_flag = False
    for node in graph:
        if node.in_degree != node.out_degree:
            return False
        # if node.in_degree - node.out_degree == 1 and first_flag:
        #     return False
        # if node.out_degree - node.in_degree == 1 and second_flag:
        #     return False
        # if node.in_degree - node.out_degree == 1:
        #     first_flag = True
        # if node.out_degree - node.in_degree == 1:
        #     second_flag = True
    return True


# n: vertices
# m: edges
if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    graph = build_graph(n, m, edges)
    if not is_path_available(graph):
        print('0')
    print('1')
    path = find_eulerian_cycle(graph)
    result = ""
    for p in path:
        result += str(p) + " "
    print(result)

'''
3 4
2 3
2 2
1 2 
3 1
'''

'''
3 4 
1 3 
2 3 
1 2 
3 1
'''

'''
4 7
1 2
2 1
1 4
4 1
2 4
3 2
4 3
'''

'''
4 7
2 3
3 4
1 4
3 1
4 2
2 3
4 2
'''
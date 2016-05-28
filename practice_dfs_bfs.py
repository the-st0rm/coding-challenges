#!/usr/bin/env python



graph = {'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['E','C'])}


def dfs(graph, start, Visited=None):
    
    visited = set()
    stack = ['A']
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in graph[vertex]-set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path+[next_node]))
                


print list(dfs_paths(graph, 'A', 'F'))
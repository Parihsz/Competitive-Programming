"""
BFS is an algorithm for searching a graph
It progresses horizontally and then vertically
It uses a queue, which gets processed
Here's a simple demo of it, just to understand the jist
"""

def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
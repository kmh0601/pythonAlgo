# BJ 11725

import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]
parent = [[]for _ in range(N+1)]

visited = [False] * (N+1)

for i in range(N-1):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, V, visited, parent):
    visited[V] = True

    for v in graph[V]:
        if not visited[v]:
            parent[v] = V
            dfs(graph, v, visited, parent)

dfs(graph, 1, visited, parent)

for node in parent[2:]:
    print(node)
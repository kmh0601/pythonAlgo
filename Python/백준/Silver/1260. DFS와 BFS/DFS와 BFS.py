# BJ 1206
from collections import deque

N, M, V = map(int, input().split(" "))

graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def dfs(graph, V, visited):
    print(V, end=" ")
    visited[V] = True
    for v in graph[V]:
        if not visited[v]:
            dfs(graph, v, visited)

def bfs(graph, V, visited):
    print(V, end=" ")
    visited[V] = True
    queue = deque([V])

    while queue:
        v = queue.popleft()

        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                print(node, end=" ")
                visited[node] = True

visited = [False] * (N+1)
dfs(graph=graph, V=V, visited=visited)
print()
visited = [False] * (N+1)
bfs(graph=graph, V=V, visited=visited)
# BJ2606 바이러스
import sys
sys.setrecursionlimit(2500)

N = int(input())
M = int(input())

comGraph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for i in range(M):
    x, y = map(int,input().split(" "))
    comGraph[x].append(y)
    comGraph[y].append(x)

def dfs(comGraph,V,visited):
    visited[V] = True
    global count
    count += 1

    for i in comGraph[V]:
        if not visited[i]:
            dfs(comGraph, i, visited)

dfs(comGraph,1,visited)

print(count-1)
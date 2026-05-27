# When to use:
# All edges have equal weight (usually 1)

edges = [[0,1],[0,3],[3,4],[4 ,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
n = 9
adj = []
for i in range(n):
    adj.append([])

for i in range(len(edges)):
    u = edges[i][0]
    v = edges[i][1]
    adj[u].append(v)

print(adj)
distance = [float('inf')]*len(adj)
print(distance)
from collections import deque
src = 0
q = deque()
q.append(0)
distance[src] = 0

while q:
    node = q.popleft()
    for it in adj[node]:
        if distance[node] + 1 < distance[it]:
            distance[it] = distance[node] + 1
            q.append(it)

print(distance) 

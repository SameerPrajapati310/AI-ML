"""
Both DFS-based Topological Sort and Kahn's Algorithm are applied to the same type of graph: a Directed Acyclic Graph (DAG). 
They are simply two different ways to compute a topological ordering.

"""
from collections import deque
matrix = [
    [0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

adj = []
n = len(matrix)
m = len(matrix[0])
q = deque()

for i in range(n):
    row = []
    for j in range(m):
        if matrix[i][j] == 1:
            row.append(j)
    adj.append(row)
print(adj)

indegree = [0]*len(adj)

for i in range(len(adj)):
    for it in adj[i]:
        indegree[it] += 1

print(indegree)
for i in range(len(indegree)):
    if indegree[i] == 0:
        q.append(i)
        
ans = []
while q:
    node = q.popleft()
    ans.append(node)
    for it in adj[node]:
        indegree[it]-=1
        if indegree[it] == 0:
            q.append(it)
print(ans)





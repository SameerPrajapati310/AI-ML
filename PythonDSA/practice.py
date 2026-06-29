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
for i in range(n):
    row = []
    for j in range(m):
        if matrix[i][j] == 1:
            row.append(j)
    adj.append(row)
print(adj)

print('ADJ LIST')
for i in range(len(adj)):
    print(f'[{i}]->{adj[i]}')


indegree = [0]*len(adj)

visited = [0]*len(adj)

for i in adj:
    for it in i:
        indegree[it] += 1
from collections import deque
q = deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        q.append(i)
ans = []
while q:
    node = q.popleft()
    ans.append(node)
    for it in adj[node]:
        indegree[it] -= 1
        if indegree[it] == 0:
            q.append(it)
print(ans)
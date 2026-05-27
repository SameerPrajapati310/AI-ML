matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

adj = []
n = len(matrix)
m = len(matrix[0])
for i in range(n):
    temp = []
    for j in range(m):
        if matrix[i][j] == 1:
            temp.append(j)
    adj.append(temp)

print('ADJ LIST')
for i in range(len(adj)):
    print(f'[{i}]->{adj[i]}')

# Bfs Traversal
from collections import deque
visited = [0]*len(adj)
visited[0] = 1
q = deque()
q.append(0)
ans = []
ans.append(0)
while q:
    node = q.popleft()
    for it in adj[node]:
        if visited[it] == 0:
            visited[it] = 1
            q.append(it)
            ans.append(it)

print()  
print('BFS Traversal')
print(ans)

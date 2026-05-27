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


def dfs(node,visited,adj):
    ans.append(node)
    visited[node] = 1
    for it in adj[node]:
        if not visited[it]:
            dfs(it,visited,adj)

visited=[0]*len(adj)
ans = []
dfs(0,visited,adj)
print()
print('DFS')
print(ans)
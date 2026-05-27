matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

# matrix = [
#     [0, 1, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0]
# ]

adj = []
for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            temp.append(j)
    
    adj.append(temp)

print(adj)


def dfs(node, parent, visited, adj):
    visited[node] = 1

    for it in adj[node]:
        if not visited[it]:
            if dfs(it, node, visited, adj):
                return True
        elif it != parent:
            return True

    return False

visited=[0]*len(adj) 
dfs(0,-1,visited,adj)


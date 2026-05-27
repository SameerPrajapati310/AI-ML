matrix = [
    [0, 1, 0, 0, 0],  # 0 -> 1
    [0, 0, 1, 0, 0],  # 1 -> 2
    [1, 0, 0, 1, 0],  # 2 -> 0 and 2 -> 3
    [0, 0, 0, 0, 1],  # 3 -> 4
    [0, 0, 0, 0, 0]
]

adj = []
n = len(matrix)
m = len(matrix[0])

for i in range(n):
    row = []
    for j in  range(m):
        if matrix[i][j] == 1:
            row.append(j)
    adj.append(row)

print(adj)
visited = [0]*len(adj)
dfsvisited = [0]*len(adj)

def isCycle(node,visited,dfsvisited,adj):
    visited[node] = 1
    dfsvisited[node] = 1

    for it in adj[node]:
        if not visited[it]:
            isCycle(it,visited,dfsvisited,adj)
        elif dfsvisited[it]:
            return True
    
    dfsvisited[node] = 0
    return False


for i in range(len(adj)):
    if not visited[i]:
        if isCycle(i,visited,dfsvisited,adj):
            print("Cycle Detected")           
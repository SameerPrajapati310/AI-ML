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

from collections import deque           
def detect(adj,visited):
    q = deque()
    q.append((0,-1))
    visited[0] = 1
    while q:
        node,parent = q.popleft()
        for it in adj[node]:
            if not visited[it]:
                visited[it] = 1
                q.append((it,node))
            elif parent != it:
                print("Cycle detected!!!")
                return True
    print("No cycle Detected!!!")
    return False

visited = [0]*len(adj)
detect(adj,visited)

          
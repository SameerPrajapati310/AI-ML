"""
Both DFS-based Topological Sort and Kahn's Algorithm are applied to the same type of graph: a Directed Acyclic Graph (DAG). 
They are simply two different ways to compute a topological ordering.

"""

matrix = [
    [0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

class stack:
    def __init__(self):
        self.ans = []
    def push(self,value):
        self.ans.append(value)
    def pop(self):
        if len(self.ans) == 0:
            print("Error stack is empty")
            return None
        return self.ans.pop()
    def top(self):
        if len(self.ans) == 0:
            print("Stack is empty")
            return None
        return self.ans[-1]
    def size(self):
        return len(self.ans)

n = len(matrix)
m = len(matrix[0])
s = stack()
adj = []

for i in range(n):
    row = []
    for j in range(m):
        if matrix[i][j] == 1:
            row.append(j)
    adj.append(row)
print(adj)


visited = [0]*len(adj)

def find(node, adj, visited, s):

    visited[node] = 1

    for it in adj[node]:
        if not visited[it]:
            find(it, adj, visited, s)
    s.push(node)

for i in range(len(adj)):
    if not visited[i]:
        find(i, adj, visited, s)

ans = []
while s.size()>0:
    ans.append(s.top())
    s.pop()

print(ans)

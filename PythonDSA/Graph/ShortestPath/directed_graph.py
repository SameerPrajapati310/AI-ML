# Graph is a DAG (Directed Acyclic Graph)
# Works with:
# Positive weights 
# Negative weights 
edges = [[0,4,2], [0,5,3], [5,4,1], [4,6,3], [4,2,1], [6,1,2], [2,3,3], [1,3,1]]
n = 7

class stack:
    def __init__(self):
        self.ans = []

    def push(self,value):
        self.ans.append(value)

    def pop(self):
        return self.ans.pop()

    def size(self):
        return len(self.ans)

    def top(self):
        if len(self.ans) > 0:
            return self.ans[-1]
        return 0

adj = []
for i in range(n):
    adj.append([])

print(adj)

for i in range(len(edges)):
    u = edges[i][0]
    v = edges[i][1]
    wt = edges[i][2]

    adj[u].append((v,wt))

print(adj)

def toppo(node,adj,visited,s):
    visited[node] = 1
    for it,wt in adj[node]:
        print(it)
        if not visited[it]:
            toppo(it,adj,visited,s)
    print(node)
    s.push(node)

s = stack()
visited = [0]*len(adj)
distance = [float('inf')]*len(adj)
distance[s.top()] = 0


toppo(0,adj,visited,s)

while s.size()>0:
    node = s.pop()
    for it,wt in adj[node]:
        if distance[node] + wt  < distance[it]:
            distance[it] = distance[node] + wt 

print(distance)
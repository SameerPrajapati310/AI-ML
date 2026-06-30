edges = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 1],
    [4, 2, 2]
]
s = set()
for i in range(len(edges)):
    s.add(edges[i][0])

adj = []
for _ in range(len(s)):
    adj.append([])

for i in range(len(adj)):
    u = edges[i][0]
    v = edges[i][1]
    wt = edges[i][2]
    adj[u].append((v,wt))

class Solution:
    def __init__(self,n):
        self.parent = []
        self.rank = [0]*n
        for i in range(n):
            self.parent.append(i)
    def findUparent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUparent(self.parent[node])
        return self.parent[node]
    def Union(self,u,v):
        ulp_u = self.findUparent(u)
        ulp_v = self.findUparent(v)
        if ulp_u == ulp_v:
            return 
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v

        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u         
        else:
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_v] += 1
        
        
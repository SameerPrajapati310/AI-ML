# Unidirected graph -> que
#DAG -> Topological sort -> only advantage it can work in -ve weights
#Dijakasta -> uni/dircted, cycle anything but not negative weight
#bellmon -> negative wieghts can detect cycle.

class Solution:
    def unidirected(self,adj):
        from collections import deque
        q = deque()
        q.append(0)
        distance = [float('inf')]*len(adj)
        distance[0] = 0
        while q:
            node = q.popleft()
            for it in adj[node]:
                if distance[node] + 1 < distance[it]:
                    distance[it] = distance[node] + 1
                    q.append(it)
        return distance
    def find(self,node,adj,s,visited):
        visited[node] = 1
        for it in adj[node]:
            if visited[it] != 1:
                self.find(it,adj,s,visited)
        s.append(node)

    def Dag(self,adj):
        s = []
        visited = [0]*len(adj)
        for i in range(len(adj)):
            if not visited[i]:
                self.find(i,adj,s,visited)
        
        distance = [float('inf')]*len(adj)
        distance[0] = 0
        while len(s) > 0:
            node = s.pop()
            wt = distance[node]
            for it,new_wt in adj[node]:
                if wt + new_wt < distance[it]:
                    distance[it] = wt+new_wt
        return distance
    def dijkstra(self,adj):
        pq = []
        import heapq
        heapq.heappush(pq,(0,0))
        distance = [float('inf')]*len(adj)

        while pq:
            wt,node = heapq.heappop(pq)
            for it,new_wt in adj[node]:
                if new_wt + wt < distance[it]:
                    distance[it] = new_wt + wt
                    heapq.heappush(pq,(distance[it],it))
        return distance

    def bellmen(self,adj):
        n = len(adj)
        
        distance = [float('inf')]*len(adj)
        for i in range(n-1): # n== number of node
            for u,v,wt in adj:
                if distance[u] != float('inf') and distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt
        return distance


class DisjointSet:
    def __init__ (self,n):
        self.parent = [] 
        self.rank = [0]*n 
        for i in range(n):
            self.parent.append(i)   
    def findUlp(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUlp(self.parent[node])
        return self.parent[node]
    def Union(self,u,v):
        ulp_u = self.findUlp(u)
        ulp_v = self.findUlp(v)
        if ulp_u == ulp_v:
            return 
        if self.rank[ulp_v] > self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_u] += 1
    def dijoint(self,edges):
        edges.sort(key=lambda x : x[2])
        merger_edg = []
        mrg_wt = 0
        for u,v,wt in edges:
            if self.findUlp(u) != self.findUlp(v):
                mrg_wt += wt
                merger_edg.append((u,v,wt))
                self.Union(u,v)
        return merger_edg,mrg_wt


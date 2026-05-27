edges = [[0,4,2], [0,5,3], [5,4,1], [4,6,3], [4,2,1], [6,1,2], [2,3,3], [1,3,1]]
n = 7

adj = []
for i in range(n):
    adj.append([])

for i in range(len(edges)):
    u = edges[i][0]
    v = edges[i][1]
    wt = edges[i][2]

    adj[u].append((v,wt))

print(adj)

visited = [0]*len(adj)
distance = [float('inf')]*len(adj)

import heapq
pq = []
distance[0] = 0
heapq.heappush(pq,(0,0))

while pq:
    wt,node = heapq.heappop(pq)
    for it,newwt in adj[node]:
        if wt + newwt < distance[it]:
            distance[it] = wt+newwt
            heapq.heappush(pq,(distance[it],it))
print(distance)
adj = [[[1,1], [2,6]],[[2,3], [0,1]],[[1,3], [0,6]]]

import heapq
pq = []
heapq.heappush(pq,(0,0))

distance = [float('inf')]*len(adj)

distance[0] = 0
while pq:
    w,node = heapq.heappop(pq)
    for it,nwt in adj[node]:
        if w + nwt < distance[it]:
            distance[it] = w + nwt
            heapq.heappush(pq,(distance[it],it))
    
print(distance)
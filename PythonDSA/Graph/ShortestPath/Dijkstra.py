# Graph has weights
# All weights are non-negative

import heapq

adj = [[[1,1], [2,6]],[[2,3], [0,1]],[[1,3], [0,6]]]

pq = []
heapq.heappush(pq, (0, 0))  

distance = [float('inf')] * len(adj)
distance[0] = 0

while pq:
    wt, node = heapq.heappop(pq)
    print(node)
    it,new_wt = adj[node]
    print("Node",it)
    print("weight",new_wt)
    for it, new_wt in adj[node]:
        if wt + new_wt < distance[it]:
            distance[it] = wt + new_wt
            heapq.heappush(pq, (distance[it], it))

print(distance)